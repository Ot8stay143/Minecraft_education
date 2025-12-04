agent.teleport_to_player()
def build_pyramid(size: int):
    # Put agent in safe place
    agent.teleport_to_player()
    agent.move(FORWARD, 3)
    agent.move(UP, 1)

    layer = 0

    while size - 2 * layer > 0:
        length = size - 2 * layer
        build_square(length)

        # go to next layer
        agent.move(UP, 1)
        agent.move(FORWARD, 1)
        agent.move(LEFT, 1)

        layer += 1


def build_square(n: int):
    # builds a hollow square
    for side in range(4):
        for step in range(n - 1):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.turn(RIGHT)


def on_chat(size):
    build_pyramid(size)

player.on_chat("pyramid", on_chat)
