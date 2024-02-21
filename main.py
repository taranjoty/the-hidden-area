def on_mob_killed():
    mobs.spawn(mobs.monster(ZOMBIE), pos(200, 200, 200))
mobs.on_mob_killed(mobs.monster(GHAST), on_mob_killed)

mobs.spawn(mobs.monster(GHAST), pos(0, 0, 0))