from crusader_bot.timer import Timer, TimerStat

def test_init_initializes_vars_properly():
    timer = Timer(max_ticks = 1)
    assert timer.get_status() == TimerStat.INITIALIZED
    assert timer.get_ticks() == 0

def test_start_initializes_vars_properly():
    timer = Timer()
    timer.start()
    assert timer.get_status() == TimerStat.RUNNING
    assert timer.get_ticks() == 0

def test_tick_increases_ticks():
    timer = Timer(max_ticks = 2)
    timer.start()
    timer.tick()
    assert timer.get_status() == TimerStat.RUNNING
    assert timer.get_ticks() == 1

def test_tick_will_expire_when_it_reaches_max_ticks():
    timer = Timer(max_ticks = 2)
    timer.start()
    timer.tick()
    assert timer.get_status() == TimerStat.RUNNING
    assert timer.get_ticks() == 1
    timer.tick()
    assert timer.get_status() == TimerStat.EXPIRED
    assert timer.get_ticks() == 2