import constants
from game.scripting.action import Action
from game.shared.point import Point

#Added later by teacher, originally found on lines 38-51
LEFT = Point(-constants.CELL_SIZE, 0)
RIGHT = Point(constants.CELL_SIZE, 0)
UP = Point(0, -constants.CELL_SIZE)
DOWN = Point(0, constants.CELL_SIZE)

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = RIGHT #Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a') and self._direction != RIGHT: #After 'and' was added by teacher
            self._direction = LEFT #Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d') and self._direction != LEFT:
            self._direction = RIGHT #Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w') and self._direction != DOWN:
            self._direction = UP #Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s') and self._direction != UP:
            self._direction = DOWN #Point(0, constants.CELL_SIZE)
        
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        opposite_head_velocity = head.get_velocity().reverse()

        if self._direction.equals(opposite_head_velocity) == False: #I added To fix bug where snake turns 180 degrees, which I think works better
            snake.turn_head(self._direction)

        