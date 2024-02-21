mobs.onMobKilled(mobs.monster(GHAST), function on_mob_killed() {
    mobs.spawn(mobs.monster(ZOMBIE), pos(200, 200, 200))
})
mobs.spawn(mobs.monster(GHAST), pos(0, 0, 0))
