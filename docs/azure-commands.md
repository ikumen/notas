# Azure CLI

Here are some common Azure CLI commands by subgroup.

###### Account, Config
```shell
# Set default Subscription
az account set \
--subscription <subscription id>

# List locations
az account list-locations \
--query "[].[displayName, id, name]"

# Setting default resource/locations
az configure --defaults \
group=<group name> \
location=<location name>

# List defaults
az configure --list-defaults
```

###### Resource Groups
```shell
# Create a Resource Group
az group create \
--name <name> \
--location <location> 
```

###### App Service and Plans

Note, `az webapp` command is for the managing an App Service (e.g Web Apps, API Apps, or Mobile Apps), while `az appservice` is for managing an [App Service Plan](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans).

```shell
# List available locations for a sku
az appservice list-locations \
--sku <sku name>

# List available runtimes
az webapp list-runtimes

# List app service plans
az appservice plan list

# Create an app service plan 
# https://docs.microsoft.com/en-us/cli/azure/appservice/plan?view=azure-cli-latest#az_appservice_plan_create
az appservice plan create \
--name <name>
--resource-group <res group> \
--location <loc> \
--hyper-v -or- --is-linux \
--sku <sku>

# Create an app service
az webapp create \
  --name $appService \
  --resource-group <res group> \
  --plan <app service plan> \
  --runtime "lang|version (e,g python|3.6)"

# Get an app service deployment publish profile
az webapp deployment list-publishing-profiles \
--name <app service> \
--xml 
```


