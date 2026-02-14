def on_button_pressed_a():
    global Menu, Player_X
    if Menu == 1:
        pass
    elif Menu == 2:
        pass
    elif Menu == 4:
        music.set_volume(255)
        basic.pause(100)
        music.play(music.tone_playable(880, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(988, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        Menu = 3
    else:
        if Player_X == Car_X and Player_Y == Car_Y:
            pass
        else:
            if Player_X == 0:
                pass
            else:
                led.unplot(Player_X, Player_Y)
                Player_X += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Score, Car_Y, Car_X, Player_X, Player_Y, Menu
    if Menu == 2:
        music.play(music.tone_playable(880, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(988, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        Score = 0
        Car_Y = 0
        Car_X = randint(0, 4)
        Player_X = 2
        Player_Y = 3
        Menu = 5
    else:
        pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Menu, Player_X
    if Menu == 1:
        pass
    elif Menu == 2:
        pass
    elif Menu == 4:
        basic.pause(100)
        Menu = 3
    else:
        if Player_X == Car_X and Player_Y == Car_Y:
            pass
        else:
            if Player_X == 4:
                pass
            else:
                led.unplot(Player_X, Player_Y)
                Player_X += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

Score = 0
Car_Y = 0
Player_Y = 0
Car_X = 0
Player_X = 0
Menu = 0
music.set_volume(0)
basic.clear_screen()
Menu = 4

def on_forever():
    if Menu == 0:
        while Menu == 0:
            for index in range(8):
                music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
                    music.PlaybackMode.UNTIL_DONE)
                basic.pause(40)
            music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            basic.pause(50)
            music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
                music.PlaybackMode.UNTIL_DONE)
            basic.pause(50)
            music.play(music.tone_playable(294, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            basic.pause(50)
            music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
                music.PlaybackMode.UNTIL_DONE)
            basic.pause(50)
            music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            basic.pause(50)
    else:
        pass
basic.forever(on_forever)

def on_forever2():
    global Menu, Car_Y, Score, Car_X
    # Menu 0 = Game
    # 
    # Menu 1 = Game Over
    # 
    # Menu 2 = Main Menu
    # 
    # Menu 3 = Intro
    if Menu == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            """)
        basic.show_leds("""
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            """)
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(880, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(784, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(698, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(659, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(587, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(200)
        music.play(music.tone_playable(220, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(208, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(196, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.clear_screen()
        basic.pause(1000)
        basic.show_string("GAMEOVER")
        basic.show_string("SCORE:")
        basic.show_number(Score)
        basic.pause(1000)
        Menu = 2
        basic.clear_screen()
    elif Menu == 2:
        basic.show_string("A+B")
        basic.clear_screen()
    elif Menu == 3:
        basic.clear_screen()
        basic.show_leds("""
            . # # # .
            # . . . #
            # # . # #
            # . . . #
            . # # # .
            """)
        music.play(music.tone_playable(587, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(784, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(880, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(988, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(1000)
        basic.show_string(" LIGHTDRIVE")
        Menu = 2
    elif Menu == 0:
        basic.clear_screen()
        if Player_X == Car_X and Player_Y == Car_Y:
            Menu = 1
        else:
            led.plot(Player_X, Player_Y)
            if Car_Y != 4:
                led.plot(Car_X, Car_Y)
                basic.pause(175)
                led.unplot(Car_X, Car_Y)
                Car_Y += 1
            else:
                led.plot(Car_X, Car_Y)
                basic.pause(175)
                led.unplot(Car_X, Car_Y)
                Score += 1
                Car_X = randint(0, 4)
                Car_Y = 0
    elif Menu == 4:
        basic.show_string("A")
        basic.pause(250)
        basic.show_leds("""
            . . # . .
            # # # . #
            # # # # #
            # # # . #
            . . # . .
            """)
        basic.pause(750)
        basic.show_string("B")
        basic.pause(250)
        basic.show_leds("""
            # . # . .
            # # # . .
            # # # . .
            # # # # .
            . . # . #
            """)
        basic.pause(750)
    elif Menu == 5:
        basic.show_string("GO!")
        Menu = 0
    else:
        music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("ERROR")
basic.forever(on_forever2)
