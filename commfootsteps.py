"""
Texts: Martin's father goes for a jog every morning. Martin follows him several minutes later. His father starts at a position that is X₁ meters away from their home and runs rectilinearly at a constant speed of V₁ meters per step for N steps.

Martin is standing at X₂ meters away from his home. He wonders how fast he must run at some constant speed of V₂ meters per step so as to maximize F, where F equals the number of his father's footsteps that Martin will land on during his run. It is given that the first step that Martin will land on, from his starting position, will have been landed on by his father.

Note that if more than one prospective velocity results in the same number of maximum common steps, output the highest prospective velocity as V₂.

Write an algorithm to help Martin calculate F and V₂.

Input:
The first line of the input consists of an integer fatherPos, representing the initial position of Martin's father .
The second line consists of an integer martinPos, representing the initial position of Martin (X₂).
The third line consists of an integer velFather, representing the velocity of the father (V₁).
The last line consists of an integer steps, representing the number of steps taken by the father (N).

Output:
Print two space-separated integers as the maximum number of common footsteps F and respective speed V₂.
"""


def main():
    try:
        father_pos = int(input("fatherPos(X₁)"))
        martin_pos = int(input("martinPos(X₂)"))
        vel_father = int(input("velFather(V₁)"))
        father_steps = int(input("fatherPos(N)"))

        print(common_foot_steps(father_pos, martin_pos, vel_father, father_steps))
    except:
        print("Please input int value. Try again.")


def common_foot_steps(father_pos: int, martin_pos: int, vel_father: int, father_steps: int) -> tuple:
    common_steps = 0  # F
    vel_martin = 0  # V2

    for i in range(father_steps + 1):
        temp_common_steps = 0
        temp_vel_martin = father_pos - martin_pos + vel_father * i

        if temp_vel_martin == 0:
            continue

        for j in range(i, father_steps + 1):
            if (father_pos - martin_pos + vel_father * j) % temp_vel_martin == 0:
                temp_common_steps = temp_common_steps + 1
        if common_steps <= temp_common_steps:
            common_steps = temp_common_steps
            vel_martin = temp_vel_martin
    return common_steps, vel_martin


if __name__ == "__main__":
    print(common_foot_steps(3, 2, 2, 20))
