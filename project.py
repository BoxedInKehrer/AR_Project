import time
from matplotlib.table import table
import numpy as np
import robotic as ry
from argparse import ArgumentParser

def quat_angle_error(q1: np.ndarray, q2: np.ndarray) -> float:
    q1 = q1 / np.linalg.norm(q1)
    q2 = q2 / np.linalg.norm(q2)
    dot = np.clip(np.abs(np.dot(q1, q2)), -1.0, 1.0)
    return 2.0 * np.arccos(dot)
class SimWrapper:
    def __init__(self, cfg: ry.Config, sim_tau: float = 5e-2, display_delay: float = 1e-1, verbose: int = 2):
        """
        Wrapper for the simulation class in robotic.

        Params:
            cfg: The ry configuration object.
            tau_sim: the inverse frequency of the simulation.
            display_delay: how much delay the visualization receives if activated. Useful for debugging.
            verbose: In addition to console logs, this turns on the visualization of the sim (weird overload, I know).
                Use verbose = 2 to visualize the rollouts.
        """
        self.cfg = cfg
        self.sim = ry.Simulation(cfg, engine=ry.SimulationEngine.physx, verbose=verbose)
        self.sim_tau = sim_tau
        self.display_delay = display_delay
        self.verbose = verbose
        self.q_home = self.sim.getState()
        self.reset()

    def reset(self):
        self.sim.resetTime(0.)
        self.sim.resetSplineRef()
        self.sim.setState(*self.q_home)

    def step(self, u: np.ndarray | list, mode: ry.ControlMode) -> None:
        self.sim.step(u, self.sim_tau, mode)
        if self.verbose > 1 and self.display_delay > 0:
            time.sleep(self.display_delay)

    def set_spline_ref(self, path: np.ndarray | list, times: np.ndarray | list) -> None:
        self.sim.setSplineRef(path, times)

    def close_gripper(self, gripper_name: str = "l_gripper", tol: float = 1e-6):
        self.sim.moveGripper(gripper_name, 0.)
        while self.sim.getGripperWidth(gripper_name) >= tol:
            self.step([], ry.ControlMode.none)

    def run_trajectory(self, path: np.ndarray | list, n_phases: int):
        """Run a full trajectory.

        Params:
            path: The full sequence of control targets.
            n_phases: How many phases should be used,
                determines the coarseness of the simulation.
        """
        path = np.atleast_2d(path)

        # 1.: Simulated trajectory rollout
        # This code snippet should complete the rollout of a trajectory in simulation

        #### BEGIN SOLUTION
        times = np.linspace(0, n_phases, len(path))
        self.set_spline_ref(path, times)
        n_steps = int(np.ceil(n_phases / self.sim_tau))
        for _ in range(n_steps):
            self.step([], ry.ControlMode.spline)
        #### END SOLUTION
    

# def push(cfg: ry.Config) -> ry.KOMO:
    

#     return komo


def main(args):
    cfg = ry.Config()
    cfg.addFile(ry.raiPath("scenarios/pandaSingle.g"))
    cfg.delFrame("panda_collCameraWrist")
    cfg.addFile("configs/cfg.g")


    table = cfg.getFrame("table")
    orig = table.getSize()
    table.setShape(ry.ST.ssBox, [1.5, 3.0, orig[2], orig[3]])

    cfg.view(pause=True)



    n_phases = 5
    # q_home = cfg.getJointState()


    # komo = push(cfg)
    # sol = ry.NLP_Solver()
    # sol.setProblem(komo.nlp())
    # sol.setOptions(damping=1e-1, verbose=0, stopTolerance=1e-2, stopInners=100, stopEvals=1000)
    # ret = sol.solve()
    # print(f"Solution found is {'' if ret.feasible else 'not'} feasible.")

    # path = komo.getPath()
    # komo.view_play(False, delay=.1)

    # if not args.botop:
    #     sim = SimWrapper(cfg, display_delay=0.1)
    #     sim.close_gripper()
    #     sim.run_trajectory(path, n_phases=n_phases)
    #     for _ in range(100):
    #         sim.step([], ry.ControlMode.none)
    #     sim.reset()

    
    # Execution on botop
    # else:
    #     bot = ry.BotOp(C=cfg, useRealRobot=args.real)
    #     bot.wait(cfg, forKeyPressed=False, forTimeToEnd=True)
    #     bot.moveTo(q_home)
    #     # Close gripper
    #     bot.gripperMove(ry.ArgWord._left, 0.)
    #     bot.wait(cfg, forKeyPressed=False, forTimeToEnd=True)
    #     # Run reference path
    #     times = np.linspace(0, n_phases, path.shape[0])
    #     bot.move(path, times)
    #     bot.wait(cfg, forKeyPressed=False, forTimeToEnd=True)


if __name__ == "__main__":
    args = None

    p = ArgumentParser()
    p.add_argument("--botop", action="store_true", default=False, help="Use botop in addition to the simulator for a comparison.")
    p.add_argument("--real", action="store_true", default=False,
                   help="Use this arg if real robot is used")
    args = p.parse_args()

    print(args)

    if args.real and not args.botop:
        p.error("--real can only be used with --botop")

    main(args)
