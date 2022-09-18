#!/bin/sh -e

my_ip=$(curl -q ifconfig.co 2> /dev/null)
IFS=, read -a subdomains <<< $1
for subdomain in "${subdomains[@]}"
do
  domain=$subdomain.duckdns.org
  echo "comparing $my_ip against $domain"
  [ "$my_ip" == "$(getent hosts $domain | awk '{ print $1 }')" ] || exit 1
done
