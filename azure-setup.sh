#!/bin/bash

resourceGroup="notas-resgrp"
location="westus2"
appServicePlan="notas-asp"
appService="notas-as"
appServiceRuntime="python|3.6"

echo "Creating Resource Group ${resourceGroup}..."
if [ $(az group exists --name ${resourceGroup}) == false ]; then
  az group create \
  --name $resourceGroup \
  --location $location
  --verbose
  echo "Resource Group ${resourceGroup} created!"
else
  echo "Resource Group ${resourceGroup} exists, skipping creation"
fi

echo ""
echo "Setting default group=${resourceGroup}, location=${location}"
az configure --defaults \
group="${resourceGroup}" \
location="${location}"

echo ""
echo "Create App Service Plan ${appServicePlan}..."
if [ "$(az appservice plan list --query "[?name=='${appServicePlan}'].[name]")" == "[]" ]; then
  az appservice plan create \
  --name $appServicePlan \
  --is-linux \
  --sku FREE
  echo "App Service Plan ${appServicePlan} created!"
else
  echo "App Service Plan ${appServicePlan} exists, skipping creation"
fi

echo ""
echo "Creating App Service ${appService}..."
if [ "$(az webapp list --query "[?name=='${appService}'].[name]")" == "[]" ]; then
  az webapp create \
  --name $appService \
  --plan $appServicePlan \
  --runtime "${appServiceRuntime}"
  echo "App Service ${appService} created!"
else
  echo "App Service ${appService} exists, skipping creation"
fi
