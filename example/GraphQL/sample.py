# Import the requests module as it allows
# us to request to the api.
import requests

# NOTE: This is for requesting a GraphQL response
#       without any authorization (bearer token | access_token)

# The GraphQL url to request which can be:
# - https://graphql.epicgames.com/graphql [Main Site]
# - https://epicgames.com/graphql [Counter Part Of Main Site]
# - https://graphql.epicgames.com/partyhub/graphql [Fortnite Party Hub]
# - https://graphql.unrealengine.com/ue/graphql [Unreal Engine Documentation]
# (NOTE: each one could have different requirements depending on what you want to achieve)
url = 'https://graphql.epicgames.com/graphql'

# The method which you are trying to request
# but just remember:
#
# 1. An operation request that includes a query
#    in the url is always GET.
#
# 2. If the request you are trying to request
#    includes a JSON objected passed along as
#    json (payload), means that it is a POST.
method = 'POST'

# The query which we will be parsing into a
# one lined query string.

# NOTE: The one provided below is a template
# NOTE: query for getting invites, suggested friends
# NOTE: linked account activity, and recent players
# NOTE: you've plaed with.

# NOTE: This query can be matched with a Cookie to
# NOTE: give data depending on the account.
query = """query feedQuery($locale: String!, $countryCode: String) {
  TransientStream {
    myTransientFeed(countryCode: $countryCode, locale: $locale) {
      id
      activity {
        ... on LinkAccountActivity {
          type
          created_at
          platforms
        }
        ... on SuggestedFriendsActivity {
          type
          created_at
          platform
          suggestions {
            epicId
            epicDisplayName
            platformFullName
            platformAvatar
          }
        }
        ... on IncomingInvitesActivity {
          type
          created_at
          invites {
            epicId
            epicDisplayName
          }
        }
        ... on RecentPlayersActivity {
          type
          created_at
          players {
            epicId
            epicDisplayName
            playedGameName
          }
        }
      }
    }
  }
}"""

# The variables that act as a replacer
# for the variables in the query that have
# "$...: ..!" meaning that it'll be replaced
# with the same variable name from this object.

# Make sure to search throughout the query to find
# the variables you need to provide.
variables = {
    "locale": "en-US",
    "countryCode": "US"
}

# Now we are finally going to request to the
# GraphQL endpoint for the response.
request = requests.request(
    method = method,
    url = url,
    json = { # Here we place the query and variables..
        "query": ' '.join(query.split()).replace('\n', ''), # (makes it have no new lines nor large tabs)
        "variables": variables
    }
)

# Print out the request
print(request.json())