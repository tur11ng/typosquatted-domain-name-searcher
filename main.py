import argparse
import asyncio
import sys
import validators

from searcher import Searcher, FilterLevel


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain_name', type=str, help='The \
                        domain name to search for typosquatted alternatives.')
    parser.add_argument('-f', '--filter-level', type=str, choices=[filter_level.name for filter_level in FilterLevel],
                        help='The filter level to perform against the domain names.')
    args = parser.parse_args(sys.argv[1:])

    domain_name = args.domain_name

    if not validators.domain(domain_name):
        raise Exception(
            'Invalid domain name. Check that the domain name you provided complies with RFCs 1034, 1035, 2181'
        )

    if args.filter_level:
        filter_level = FilterLevel[args.filter_level]
        async for domain_name, score in Searcher.search_unregistered_typosquatted_domain_names(domain_name, filter_level):
            print(f"{domain_name} : {score}")
    else:
        async for domain_name, _ in Searcher.search_unregistered_typosquatted_domain_names(domain_name):
            print(domain_name)


if __name__ == '__main__':
    asyncio.run(main())
