def postav_dom(base):
    blocks.fill(
        CONCRETE,
        base,
        positions.add(base, positions.create(7, 4, 7)),
        FillOperation.REPLACE
    )

    blocks.fill(
        AIR,
        positions.add(base, positions.create(1, 1, 1)),
        positions.add(base, positions.create(6, 3, 6)),
        FillOperation.REPLACE
    )

    blocks.fill(
        CONCRETE,
        positions.add(base, positions.create(0, 5, 0)),
        positions.add(base, positions.create(7, 5, 7)),
        FillOperation.REPLACE
    )

    blocks.place(
        BIRCH_DOOR,
        positions.add(base, positions.create(3, 1, 0))
    )

    blocks.place(
        GLASS,
        positions.add(base, positions.create(3, 2, 7))
    )

    mobs.spawn(
        mobs.animal(VILLAGER),
        positions.add(base, positions.create(3, 1, -1))
    )


def postav_strom(base):
    blocks.fill(
        LOG_OAK,
        base,
        positions.add(base, positions.create(0, 4, 0)),
        FillOperation.REPLACE
    )

    blocks.fill(
        LEAVES_OAK,
        positions.add(base, positions.create(-2, 3, -2)),
        positions.add(base, positions.create(2, 6, 2)),
        FillOperation.REPLACE
    )


def postav_studnu(base):
    blocks.fill(
        COBBLESTONE,
        base,
        positions.add(base, positions.create(4, 0, 4)),
        FillOperation.REPLACE
    )

    blocks.fill(
        AIR,
        positions.add(base, positions.create(1, 0, 1)),
        positions.add(base, positions.create(3, 0, 3)),
        FillOperation.REPLACE
    )

    blocks.fill(
        WATER,
        positions.add(base, positions.create(1, -1, 1)),
        positions.add(base, positions.create(3, -1, 3)),
        FillOperation.REPLACE
    )


def dedina():
    start_pos = player.position()

    for i in range(5):
        offset = positions.create(i * 12, 0, 0)
        base = positions.add(start_pos, offset)
        postav_dom(base)

        strom_pos = positions.add(base, positions.create(4, 0, 10))
        postav_strom(strom_pos)

   
    start = positions.add(start_pos, positions.create(0, 0, -2))
    end = positions.add(start_pos, positions.create(60, 0, -3))

    blocks.fill(
        PALE_OAK_PLANKS,
        start,
        end,
        FillOperation.REPLACE
    )

    
    studna_pos = positions.add(start_pos, positions.create(24, 0, 6))
    postav_studnu(studna_pos)


player.on_chat("dedina", dedina)
