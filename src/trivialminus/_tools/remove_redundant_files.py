"""Removes redundant TrivialMinus files."""

import logging

from good_ass_pydantic_integrator.utils import remove_redundant_files

import trivialminus

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    remove_redundant_files(trivialminus)
