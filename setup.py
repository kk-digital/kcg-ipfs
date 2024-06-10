import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="kcg-ipfs",
    py_modules=["human_eval", "llm_wrapper"],
    version="1.0",
    description="",
    author="kcg",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "evaluate_functional_correctness = human_eval.evaluate_functional_correctness:main",
            "lmstudio_eval = human_eval.eval_scripts.lmstudio_eval:main",
            "codestral_eval = human_eval.eval_scripts.codestral_eval:main",
            "openai_eval = human_eval.eval_scripts.openai_eval:main"
        ]
    }
)
