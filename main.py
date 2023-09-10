import argparse
import asyncio
import sys
import validators

from searcher import Searcher


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain_name', type=str, help='The \
                        domain name to search for typosquatted alternatives.')
    parser.add_argument('-e', '--evaluate', action='store_true',
                        help='Perform evaluation of the results')
    args = parser.parse_args(sys.argv[1:])

    domain_name = args.domain_name
    evaluate = args.evaluate

    if not validators.domain(domain_name):
        raise Exception(
            'Invalid domain name. Check that the domain name you provided complies with RFCs 1034, 1035, 2181'
        )

    if evaluate:
        async for domain_name, score in Searcher.search_unregistered_typosquatted_domain_names(domain_name, evaluate):
            print(f"{domain_name} : {score}")
    else:
        async for domain_name, score in Searcher.search_unregistered_typosquatted_domain_names(domain_name, evaluate):
            print(domain_name)


if __name__ == '__main__':
    asyncio.run(main())
