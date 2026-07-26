"""Removes redundant TrivialMinus files."""

import logging

from good_ass_pydantic_integrator.utils import remove_redundant_files

import trivial_minus

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    remove_redundant_files(trivial_minus)
