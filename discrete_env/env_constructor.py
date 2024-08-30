
from discrete_env.acrobot_pre_vec import create_acrobot
from discrete_env.cartpole_pre_vec import create_cartpole, create_cartpole_continuous
from discrete_env.cartpole_swing_pre_vec import create_cartpole_swing
from discrete_env.mountain_car_pre_vec import create_mountain_car
from discrete_env.pre_vec_wrappers import DeVecEnvWrapper, PetsWrapper


def get_env_constructor(env_name):
    if env_name == "cartpole":
        create_venv = create_cartpole
    if env_name == "cartpole_continuous":
        create_venv = create_cartpole_continuous
    if env_name == "cartpole_swing":
        create_venv = create_cartpole_swing
    if env_name == "mountain_car":
        create_venv = create_mountain_car
    if env_name == "acrobot":
        create_venv = create_acrobot
    if env_name == "lunar_lander":
        raise NotImplementedError
    return create_venv


def get_pets_env_constructor(env_name):
    env_cons = get_env_constructor(env_name)

    def pets_cons(*args, **kwargs):
        return PetsWrapper(DeVecEnvWrapper(env_cons(*args, **kwargs)))

    return pets_cons


def get_dreamer_env_constructor(env_name):
    env_cons = get_env_constructor(env_name)

    def dreamer_cons(*args, **kwargs):
        return DeVecEnvWrapper(env_cons(*args, **kwargs))

    return dreamer_cons

