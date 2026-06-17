import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

MYCOBOT280_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/home/aruna/Downloads/mycobot_280_pi_gripper.usd",
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=True,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "joint2_to_joint1": 0.0,
            "joint3_to_joint2": 0.0,
            "joint4_to_joint3": 0.0,
            "joint5_to_joint4": 0.0,
            "joint6_to_joint5": 0.0,
            "joint6output_to_joint6": 0.0,
            "gripper_controller": 0.0,
        },
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=["joint2_to_joint1", "joint3_to_joint2", "joint4_to_joint3",
                              "joint5_to_joint4", "joint6_to_joint5", "joint6output_to_joint6"],
            effort_limit=87.0,
            velocity_limit=2.175,
            stiffness=80.0,
            damping=4.0,
        ),
        "gripper": ImplicitActuatorCfg(
            joint_names_expr=["gripper_controller"],
            effort_limit=200.0,
            velocity_limit=0.2,
            stiffness=2e3,
            damping=1e2,
        ),
    },
)
