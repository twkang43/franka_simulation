import sys
from setuptools import setup, find_packages

setup(
    name="franka-valve",
    version="0.0.0.1",
    description="Rotate a valve using Franka Panda with Reinforcement Learning in mujoco simulation.",
    author=["Yujin1007", "twkang43"],
    author_email=["yujin1004k@gmail.com", "twkang43@gmail.com"],
    url="https://github.com/Yujin1007/franka_simulation",
    license="MIT",
    keywords=["reinforcement learning", "RL", "robotics", "robot", "franka", "emika", "panda"],
    platforms=[sys.platform],

    install_requires=["gym", "numpy", "gymnasium", "tensorborad", "torch", "torchvision", "torchaudio", "pytorch-cuda", "pyparsing", "stable-baselines3", "sb3-contrib", "six"],
    packages=find_packages(where="py_src"),
    package_dir={"":"py_src"},
    python_requires=">=3.8",

    classifiers=[
        "Programming Language::Python::3",
        "License :: OSI Approved :: MIT License",
        "Operating System::POSIX::Linux"
    ],
    package_data={"py_src/assets/cpp_library": ["controller.so"]},
    include_package_data=True
)