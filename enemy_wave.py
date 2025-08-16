from enemy_manager import EnemyType

class EnemySubWave:
    def __init__(self, enemy_type: EnemyType, amount: int, percent_into_wave_start: int = 0):
        self.enemy_type = enemy_type
        self.amount = amount
        # allows the sub_wave to start later in the wave/round
        self.percent_into_wave_start = percent_into_wave_start

        self.starting_tick: int = 0
        self.last_spawn_tick : int = 0
        self.ticks_to_spawn_at: int = 1 # base is 1 every tick

        self.spawned_enemies: int = 0
    
    def update_tick_info(self, starting_tick: int, ticks_to_spawn_at: int):
        self.starting_tick = starting_tick
        self.ticks_to_spawn_at = ticks_to_spawn_at

    def inc_spawned(self):
        self.spawned_enemies += 1
    
    def complete(self) ->  bool:
        return self.spawned_enemies >= self.amount


class EnemyWave:
    def __init__(self, duration_seconds: int, list_sub_waves: list[EnemySubWave]):
        self.list_sub_waves: list[EnemySubWave] = list_sub_waves
        self.duration_seconds = duration_seconds
        self.current_tick: int = 0
        self.enemies: list[EnemyType] = []

        self.init_tick_info()

    def init_tick_info(self):
        for sub_wave in self.list_sub_waves:
            starting_tick = self.current_tick + 1 if sub_wave.percent_into_wave_start == 0 else int(self.current_tick + (self.duration_seconds * sub_wave.percent_into_wave_start / 100))
            ticks_to_spawn_at = int((self.duration_seconds - self.percent_to_seconds(sub_wave.percent_into_wave_start)) * 60 ) / sub_wave.amount
            sub_wave.update_tick_info(starting_tick=starting_tick, ticks_to_spawn_at=ticks_to_spawn_at)

    def percent_to_seconds(self, percent: int) -> int:
        return int(self.duration_seconds * percent / 100)

    def update(self) -> list[EnemyType]:
        self.current_tick += 1
        enemies_to_spawn : list[EnemyType] = []
        
        for sub_wave in self.list_sub_waves:
            if sub_wave.complete():
                continue

            if self.current_tick == sub_wave.starting_tick:
                enemies_to_spawn.extend([sub_wave.enemy_type])
                sub_wave.inc_spawned()
            elif self.current_tick % sub_wave.ticks_to_spawn_at == 0:
                    enemies_to_spawn.append(sub_wave.enemy_type)
                    sub_wave.inc_spawned()

        return enemies_to_spawn


def test_enemy_wave():
    sub_wave = EnemySubWave(enemy_type=EnemyType.normal, amount=10, percent_into_wave_start=0)
    wave = EnemyWave(duration_seconds=60, list_sub_waves=[sub_wave])
    wave.init_tick_info()
    
    assert sub_wave.starting_tick == 0
    assert sub_wave.ticks_to_spawn_at == 360  # 60 seconds / 10 enemies = 6 seconds per enemy
    wave.update()
    assert wave.current_tick == 1

    # Test percent to seconds conversion
    assert wave.percent_to_seconds(50) == 30  # 50% of 60 seconds is 30 seconds