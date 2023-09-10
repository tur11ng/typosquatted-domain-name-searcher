from typing import List, Tuple, Union, AsyncGenerator

from checker import Checker
from comparator import Comparator
from generator import Generator


class Searcher:
    @staticmethod
    async def search_unregistered_typosquatted_domain_names(domain_name: str,
                                                            evaluate=False) -> AsyncGenerator[
        Tuple[str, Union[float, None]], None]:
        for typosquatted_domain_name in Generator.generate(domain_name):
            if not Checker.is_domain_name_registered(typosquatted_domain_name):
                if evaluate:
                    score = await Comparator.compare_domain_names(domain_name, typosquatted_domain_name)
                else:
                    score = None  # score is None when evaluate is False
                yield typosquatted_domain_name, score
