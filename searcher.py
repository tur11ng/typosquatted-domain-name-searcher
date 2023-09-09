from typing import List

from checker import Checker
from comparator import Comparator
from generator import Generator
from utils import OperatingSystem


class Searcher:
    @staticmethod
    def search_unregistered_typosquatted_domain_names(domain_name: str, operating_system: OperatingSystem) -> List[str]:
        for typosquatted_domain_name in Generator.generate(domain_name):
            if not Checker.is_domain_name_registered(typosquatted_domain_name):
                score = Comparator.compare_domain_names(domain_name, typosquatted_domain_name, operating_system)
                yield {typosquatted_domain_name: score}
