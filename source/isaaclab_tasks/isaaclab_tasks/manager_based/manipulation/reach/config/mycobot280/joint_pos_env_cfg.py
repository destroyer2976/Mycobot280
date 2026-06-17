import math
from isaaclab.utils import configclass
import isaaclab_tasks.manager_based.manipulation.reach.mdp as mdp
from isaaclab_tasks.manager_based.manipulation.reach.reach_env_cfg import ReachEnvCfg
from isaaclab_assets.robots.mycobot280 import MYCOBOT280_CFG

@configclass
class MyCobotReachEnvCfg(ReachEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.scene.robot = MYCOBOT280_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        self.rewards.end_effector_position_tracking.params["asset_cfg"].body_names = ["joint6_flange"]
        self.rewards.end_effector_position_tracking_fine_grained.params["asset_cfg"].body_names = ["joint6_flange"]
        self.rewards.end_effector_orientation_tracking.params["asset_cfg"].body_names = ["joint6_flange"]
        self.rewards.end_effector_orientation_tracking.weight = 0.0
        self.actions.arm_action = mdp.JointPositionActionCfg(
            asset_name="robot",
            joint_names=["joint2_to_joint1", "joint3_to_joint2", "joint4_to_joint3",
                         "joint5_to_joint4", "joint6_to_joint5", "joint6output_to_joint6"],
            scale=0.2,
            use_default_offset=True,
        )
        self.commands.ee_pose.body_name = "joint6_flange"
        self.commands.ee_pose.ranges.pos_x = (0.1, 0.25)
        self.commands.ee_pose.ranges.pos_y = (-0.15, 0.15)
        self.commands.ee_pose.ranges.pos_z = (0.2, 0.5)
        self.commands.ee_pose.ranges.pitch = (math.pi, math.pi)

@configclass
class MyCobotReachEnvCfg_PLAY(MyCobotReachEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        self.observations.policy.enable_corruption = False
