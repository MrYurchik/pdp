import asyncio


async def run_sequence(*functions) -> None:
    for function in functions:
        await function


async def run_parallel(*functions) -> None:
    await asyncio.gather(*functions)


class Radio:
    async def turn_on_radio(self) -> None:
        print('Radio turning on, estimating time 2 sec...')
        await asyncio.sleep(2)
        print('Radio TURNED ON')

    async def turn_off_radio(self) -> None:
        print('Radio turning off, estimating time 2 sec...')
        await asyncio.sleep(2)
        print('Radio TURNED OFF')

    async def play_music(self) -> None:
        print('Radio playing music, music length 2 sec...')
        await asyncio.sleep(2)
        print('Music has been played')


class Robot:
    async def turn_on_robot(self) -> None:
        print('Robot turning on, estimating time 2 sec...')
        await asyncio.sleep(2)
        print('Robot TURNED ON')

    async def clean_room(self) -> None:
        print('Robot cleaning room, estimating time 2 sec...')
        await asyncio.sleep(2)
        print('Room has been cleaned')

    async def turn_off_robot(self) -> None:
        print('Robot turning off, estimating time 2 sec...')
        await asyncio.sleep(2)
        print('Robot TURNED OFF')


class Playstation:
    async def turn_on_playstation(self) -> None:
        print('Playstation turning on, estimating time 2 sec...')
        await asyncio.sleep(2)
        print('Playstation TURNED ON')

    async def check_for_updates(self) -> None:
        print('Playstation checking for update, estimating time 2 sec...')
        await asyncio.sleep(2)
        print('Playstation has been updated')

    async def turn_off_playstation(self) -> None:
        print('Playstation turning off, estimating time 2 sec...')
        await asyncio.sleep(2)
        print('Playstation TURNED OFF')


async def main() -> None:
    radio = Radio()
    robot = Robot()
    ps = Playstation()
    print('classes initialized')
    await run_parallel(
        run_sequence(radio.turn_on_radio(),
                     radio.play_music(),
                     radio.turn_off_radio(),
                     ),
        run_sequence(robot.turn_on_robot(),
                     robot.clean_room(),
                     robot.turn_off_robot(),
                     ),
        run_sequence(ps.turn_on_playstation(),
                     ps.check_for_updates(),
                     ps.turn_off_playstation(),
                     ),
    )

if __name__ == "__main__":
    asyncio.run(main())
