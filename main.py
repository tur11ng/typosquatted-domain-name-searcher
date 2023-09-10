import argparse
import sys
import validators

from searcher import Searcher
from utils import OperatingSystem


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain_name', type=str, help='The \
                        domain name to search for typosquatted alternatives.')
    parser.add_argument('-e', '--evaluate', type=bool, default=False,
                        help='Perform evaluation of the results')
    parser.add_argument('-os', '--operating_system', type=str, choices=[os.name for os in OperatingSystem],
                        help='The operating system for which to perform the evaluation.')
    args = parser.parse_args(sys.argv[1:])

    domain_name = args.domain_name
    operating_system = args.operating_system
    evaluate = args.evaluate

    if not validators.domain(domain_name):
        raise Exception(
            'Invalid domain name. Check that the domain name you provided complies with RFCs 1034, 1035, 2181'
        )

    if evaluate:
        if operating_system:
            if operating_system not in [os.name for os in OperatingSystem]:
                raise Exception(
                    'Invalid operating system type. Check that the operating system type that you provided is supported'
                )
            else:
                operating_system = OperatingSystem[operating_system]
            for domain_name in Searcher.search_unregistered_typosquatted_domain_names(domain_name, evaluate, operating_system):
                print(domain_name)
        else:
            for domain_name in Searcher.search_unregistered_typosquatted_domain_names(domain_name, evaluate):
                print(domain_name)
    else:
        for domain_name in Searcher.search_unregistered_typosquatted_domain_names(domain_name):
            print(domain_name)


if __name__ == '__main__':
    main()
