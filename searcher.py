from enum import Enum
from typing import List, Tuple, Union, AsyncGenerator

from checker import Checker
from comparator import Comparator
from generator import Generator


class FilterLevel(Enum):
    LOW = 0.6
    MEDIUM = 0.75
    HIGH = 0.9


class Searcher:
    @staticmethod
    async def search_unregistered_typosquatted_domain_names(domain_name: str,
                                                            filter_level: FilterLevel = None) -> AsyncGenerator[
                                                                                    Tuple[str, Union[float, None]], None
                                                                               ]:
        for typosquatted_domain_name in Generator.generate(domain_name):
            if not Checker.is_domain_name_registered(typosquatted_domain_name):
                if filter:
                    score = await Comparator.compare_domain_names(domain_name, typosquatted_domain_name)
                else:
                    score = None
                if score is None or score > filter_level.value:
                    yield typosquatted_domain_name, score
