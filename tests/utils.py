import json
import os
from typing import Dict, List

from mev_inspect.schemas.blocks import Block
from mev_inspect.schemas.sandwiches import Sandwich

THIS_FILE_DIRECTORY = os.path.dirname(__file__)
TEST_BLOCKS_DIRECTORY = os.path.join(THIS_FILE_DIRECTORY, "blocks")
TEST_SANDWICHES_DIRECTORY = os.path.join(THIS_FILE_DIRECTORY, "sandwiches")


def load_test_sandwiches(block_number: int) -> List[Sandwich]:
    sandwiches_path = f"{TEST_SANDWICHES_DIRECTORY}/{block_number}.json"

    with open(sandwiches_path, "r") as file:
        sandwiches_data = json.load(file)
    return [Sandwich(**sandwich) for sandwich in sandwiches_data]


def load_test_block(block_number: int) -> Block:
    block_path = f"{TEST_BLOCKS_DIRECTORY}/{block_number}.json"
    defaults = {"block_timestamp": 0}

    with open(block_path, "r") as block_file:
        block_json = json.load(block_file)
        return Block(
            **{
                **defaults,
                **block_json,
            }
        )


def load_comp_markets() -> Dict[str, str]:
    comp_markets_path = f"{THIS_FILE_DIRECTORY}/comp_markets.json"
    with open(comp_markets_path, "r") as markets_file:
        markets = json.load(markets_file)
        return markets


def load_cream_markets() -> Dict[str, str]:
    cream_markets_path = f"{THIS_FILE_DIRECTORY}/cream_markets.json"
    with open(cream_markets_path, "r") as markets_file:
        markets = json.load(markets_file)
        return markets
