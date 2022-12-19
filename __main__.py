import constants

from cast import Cast
from food import Food
from score import Score
from cycle import Cycle
from script import Script
from control_actors_actions import ControlActorsAction
from move_actors_action import MoveActorsAction
from handle_collisions_action import HandleCollisionsAction
from draw_actors_actions import DrawActorsAction
from director import Director
from keyboard_sevice import KeyboardService
from video_service import VideoService
from color import Color
from point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("cycles", Cycle(constants.YELLOW))
    cast.add_actor("cycles", Cycle(constants.GREEN))
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction(Color))
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()