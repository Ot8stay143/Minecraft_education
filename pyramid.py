agent.teleport_to_player()
def build_pyramid(base_side):
    agent.set_slot(1)
    if base_side % 2 != 1:
        player.say("Length of base side must be odd")
    else:
        for side_length in range(base_side - 1, 0, -2):
            agent.set_assist(PLACE_ON_MOVE, True)
            for wall in range(4):
                agent.move(FORWARD, side_length)
                agent.turn_left()
            agent.move(UP, 1)
            agent.set_assist(PLACE_ON_MOVE, False)
            agent.move(FORWARD, 1)
        agent.set_assist(PLACE_ON_MOVE, True)
        agent.move(UP, 1)
player.on_chat("build", build_pyramid)
