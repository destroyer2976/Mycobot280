import gymnasium as gym
from . import agents
from .joint_pos_env_cfg import MyCobotReachEnvCfg, MyCobotReachEnvCfg_PLAY

gym.register(
    id="Isaac-Reach-MyCobot280-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    kwargs={
        "env_cfg_entry_point": MyCobotReachEnvCfg,
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:FrankaReachPPORunnerCfg",
    },
    disable_env_checker=True,
)

gym.register(
    id="Isaac-Reach-MyCobot280-Play-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    kwargs={
        "env_cfg_entry_point": MyCobotReachEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:FrankaReachPPORunnerCfg",
    },
    disable_env_checker=True,
)
