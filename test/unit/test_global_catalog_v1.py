# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from ibm_platform_services.global_catalog_v1 import *


service = GlobalCatalogV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://globalcatalog.cloud.ibm.com/api/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Object
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_catalog_entries
#-----------------------------------------------------------------------------
class TestListCatalogEntries():

    #--------------------------------------------------------
    # list_catalog_entries()
    #--------------------------------------------------------
    @responses.activate
    def test_list_catalog_entries_all_params(self):
        # Set up mock
        url = base_url + '/'
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account = 'testString'
        include = 'testString'
        q = 'testString'
        sort_by = 'testString'
        descending = 'testString'
        languages = 'testString'
        complete = 'testString'

        # Invoke method
        response = service.list_catalog_entries(
            account=account,
            include=include,
            q=q,
            sort_by=sort_by,
            descending=descending,
            languages=languages,
            complete=complete,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'include={}'.format(include) in query_string
        assert 'q={}'.format(q) in query_string
        assert 'sort-by={}'.format(sort_by) in query_string
        assert 'descending={}'.format(descending) in query_string
        assert 'languages={}'.format(languages) in query_string
        assert 'complete={}'.format(complete) in query_string


    #--------------------------------------------------------
    # test_list_catalog_entries_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_catalog_entries_required_params(self):
        # Set up mock
        url = base_url + '/'
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_catalog_entries()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_catalog_entry
#-----------------------------------------------------------------------------
class TestCreateCatalogEntry():

    #--------------------------------------------------------
    # create_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/'
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['service_staging_url'] = 'testString'
        callbacks_model['service_production_url'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString'
        object_meta_data_alias_model['plan_id'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString'
        object_meta_data_deployment_model['target_crn'] = 'testString'
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model['supports_rc_migration'] = True

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True
        object_meta_data_plan_model['reservable'] = True
        object_meta_data_plan_model['allow_internal_users'] = True
        object_meta_data_plan_model['async_provisioning_supported'] = True
        object_meta_data_plan_model['async_unprovisioning_supported'] = True
        object_meta_data_plan_model['test_check_interval'] = 38
        object_meta_data_plan_model['single_scope_instance'] = 'testString'
        object_meta_data_plan_model['service_check_enabled'] = True
        object_meta_data_plan_model['cf_guid'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString'
        object_meta_data_service_model['iam_compatible'] = True
        object_meta_data_service_model['unique_api_key'] = True
        object_meta_data_service_model['provisionable'] = True
        object_meta_data_service_model['async_provisioning_supported'] = True
        object_meta_data_service_model['async_unprovisioning_supported'] = True
        object_meta_data_service_model['cf_guid'] = 'testString'
        object_meta_data_service_model['bindable'] = True
        object_meta_data_service_model['requires'] = ['testString']
        object_meta_data_service_model['plan_updateable'] = True
        object_meta_data_service_model['state'] = 'testString'
        object_meta_data_service_model['service_check_enabled'] = True
        object_meta_data_service_model['test_check_interval'] = 38
        object_meta_data_service_model['service_key_supported'] = True

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString'
        object_meta_data_sla_model['tenancy'] = 'testString'
        object_meta_data_sla_model['provisioning'] = 'testString'
        object_meta_data_sla_model['responsiveness'] = 'testString'
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString']
        object_meta_data_template_model['default_memory'] = 38
        object_meta_data_template_model['start_cmd'] = 'testString'
        object_meta_data_template_model['source'] = object_meta_data_template_source_model
        object_meta_data_template_model['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model['cf_runtime_id'] = 'testString'
        object_meta_data_template_model['template_id'] = 'testString'
        object_meta_data_template_model['executable_file'] = 'testString'
        object_meta_data_template_model['buildpack'] = 'testString'
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString'
        pricing_model['origin'] = 'testString'
        pricing_model['starting_price'] = starting_price_model
        pricing_model['metrics'] = [metrics_model]

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['reservable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True
        object_meta_data_model['ui'] = ui_meta_data_model
        object_meta_data_model['pricing'] = pricing_model
        object_meta_data_model['compliance'] = ['testString']
        object_meta_data_model['service'] = object_meta_data_service_model
        object_meta_data_model['plan'] = object_meta_data_plan_model
        object_meta_data_model['template'] = object_meta_data_template_model
        object_meta_data_model['deployment'] = object_meta_data_deployment_model
        object_meta_data_model['alias'] = object_meta_data_alias_model
        object_meta_data_model['sla'] = object_meta_data_sla_model
        object_meta_data_model['callbacks'] = callbacks_model
        object_meta_data_model['version'] = 'testString'
        object_meta_data_model['original_name'] = 'testString'
        object_meta_data_model['other'] = { 'foo': 'bar' }

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        overview_ui = overview_ui_model
        kind = 'testString'
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        group = True
        metadata = object_meta_data_model
        active = True
        account = 'testString'

        # Invoke method
        response = service.create_catalog_entry(
            id,
            name,
            overview_ui,
            kind,
            images,
            disabled,
            tags,
            provider,
            parent_id=parent_id,
            group=group,
            metadata=metadata,
            active=active,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['overview_ui'] == overview_ui_model
        assert req_body['kind'] == 'testString'
        assert req_body['images'] == image_model
        assert req_body['disabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['provider'] == provider_model
        assert req_body['parent_id'] == 'testString'
        assert req_body['group'] == True
        assert req_body['metadata'] == object_meta_data_model
        assert req_body['active'] == True


    #--------------------------------------------------------
    # test_create_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/'
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['service_staging_url'] = 'testString'
        callbacks_model['service_production_url'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString'
        object_meta_data_alias_model['plan_id'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString'
        object_meta_data_deployment_model['target_crn'] = 'testString'
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model['supports_rc_migration'] = True

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True
        object_meta_data_plan_model['reservable'] = True
        object_meta_data_plan_model['allow_internal_users'] = True
        object_meta_data_plan_model['async_provisioning_supported'] = True
        object_meta_data_plan_model['async_unprovisioning_supported'] = True
        object_meta_data_plan_model['test_check_interval'] = 38
        object_meta_data_plan_model['single_scope_instance'] = 'testString'
        object_meta_data_plan_model['service_check_enabled'] = True
        object_meta_data_plan_model['cf_guid'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString'
        object_meta_data_service_model['iam_compatible'] = True
        object_meta_data_service_model['unique_api_key'] = True
        object_meta_data_service_model['provisionable'] = True
        object_meta_data_service_model['async_provisioning_supported'] = True
        object_meta_data_service_model['async_unprovisioning_supported'] = True
        object_meta_data_service_model['cf_guid'] = 'testString'
        object_meta_data_service_model['bindable'] = True
        object_meta_data_service_model['requires'] = ['testString']
        object_meta_data_service_model['plan_updateable'] = True
        object_meta_data_service_model['state'] = 'testString'
        object_meta_data_service_model['service_check_enabled'] = True
        object_meta_data_service_model['test_check_interval'] = 38
        object_meta_data_service_model['service_key_supported'] = True

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString'
        object_meta_data_sla_model['tenancy'] = 'testString'
        object_meta_data_sla_model['provisioning'] = 'testString'
        object_meta_data_sla_model['responsiveness'] = 'testString'
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString']
        object_meta_data_template_model['default_memory'] = 38
        object_meta_data_template_model['start_cmd'] = 'testString'
        object_meta_data_template_model['source'] = object_meta_data_template_source_model
        object_meta_data_template_model['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model['cf_runtime_id'] = 'testString'
        object_meta_data_template_model['template_id'] = 'testString'
        object_meta_data_template_model['executable_file'] = 'testString'
        object_meta_data_template_model['buildpack'] = 'testString'
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString'
        pricing_model['origin'] = 'testString'
        pricing_model['starting_price'] = starting_price_model
        pricing_model['metrics'] = [metrics_model]

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['reservable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True
        object_meta_data_model['ui'] = ui_meta_data_model
        object_meta_data_model['pricing'] = pricing_model
        object_meta_data_model['compliance'] = ['testString']
        object_meta_data_model['service'] = object_meta_data_service_model
        object_meta_data_model['plan'] = object_meta_data_plan_model
        object_meta_data_model['template'] = object_meta_data_template_model
        object_meta_data_model['deployment'] = object_meta_data_deployment_model
        object_meta_data_model['alias'] = object_meta_data_alias_model
        object_meta_data_model['sla'] = object_meta_data_sla_model
        object_meta_data_model['callbacks'] = callbacks_model
        object_meta_data_model['version'] = 'testString'
        object_meta_data_model['original_name'] = 'testString'
        object_meta_data_model['other'] = { 'foo': 'bar' }

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        overview_ui = overview_ui_model
        kind = 'testString'
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        group = True
        metadata = object_meta_data_model
        active = True

        # Invoke method
        response = service.create_catalog_entry(
            id,
            name,
            overview_ui,
            kind,
            images,
            disabled,
            tags,
            provider,
            parent_id=parent_id,
            group=group,
            metadata=metadata,
            active=active,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['overview_ui'] == overview_ui_model
        assert req_body['kind'] == 'testString'
        assert req_body['images'] == image_model
        assert req_body['disabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['provider'] == provider_model
        assert req_body['parent_id'] == 'testString'
        assert req_body['group'] == True
        assert req_body['metadata'] == object_meta_data_model
        assert req_body['active'] == True


    #--------------------------------------------------------
    # test_create_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/'
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['service_staging_url'] = 'testString'
        callbacks_model['service_production_url'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString'
        object_meta_data_alias_model['plan_id'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString'
        object_meta_data_deployment_model['target_crn'] = 'testString'
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model['supports_rc_migration'] = True

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True
        object_meta_data_plan_model['reservable'] = True
        object_meta_data_plan_model['allow_internal_users'] = True
        object_meta_data_plan_model['async_provisioning_supported'] = True
        object_meta_data_plan_model['async_unprovisioning_supported'] = True
        object_meta_data_plan_model['test_check_interval'] = 38
        object_meta_data_plan_model['single_scope_instance'] = 'testString'
        object_meta_data_plan_model['service_check_enabled'] = True
        object_meta_data_plan_model['cf_guid'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString'
        object_meta_data_service_model['iam_compatible'] = True
        object_meta_data_service_model['unique_api_key'] = True
        object_meta_data_service_model['provisionable'] = True
        object_meta_data_service_model['async_provisioning_supported'] = True
        object_meta_data_service_model['async_unprovisioning_supported'] = True
        object_meta_data_service_model['cf_guid'] = 'testString'
        object_meta_data_service_model['bindable'] = True
        object_meta_data_service_model['requires'] = ['testString']
        object_meta_data_service_model['plan_updateable'] = True
        object_meta_data_service_model['state'] = 'testString'
        object_meta_data_service_model['service_check_enabled'] = True
        object_meta_data_service_model['test_check_interval'] = 38
        object_meta_data_service_model['service_key_supported'] = True

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString'
        object_meta_data_sla_model['tenancy'] = 'testString'
        object_meta_data_sla_model['provisioning'] = 'testString'
        object_meta_data_sla_model['responsiveness'] = 'testString'
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString']
        object_meta_data_template_model['default_memory'] = 38
        object_meta_data_template_model['start_cmd'] = 'testString'
        object_meta_data_template_model['source'] = object_meta_data_template_source_model
        object_meta_data_template_model['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model['cf_runtime_id'] = 'testString'
        object_meta_data_template_model['template_id'] = 'testString'
        object_meta_data_template_model['executable_file'] = 'testString'
        object_meta_data_template_model['buildpack'] = 'testString'
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString'
        pricing_model['origin'] = 'testString'
        pricing_model['starting_price'] = starting_price_model
        pricing_model['metrics'] = [metrics_model]

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['reservable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True
        object_meta_data_model['ui'] = ui_meta_data_model
        object_meta_data_model['pricing'] = pricing_model
        object_meta_data_model['compliance'] = ['testString']
        object_meta_data_model['service'] = object_meta_data_service_model
        object_meta_data_model['plan'] = object_meta_data_plan_model
        object_meta_data_model['template'] = object_meta_data_template_model
        object_meta_data_model['deployment'] = object_meta_data_deployment_model
        object_meta_data_model['alias'] = object_meta_data_alias_model
        object_meta_data_model['sla'] = object_meta_data_sla_model
        object_meta_data_model['callbacks'] = callbacks_model
        object_meta_data_model['version'] = 'testString'
        object_meta_data_model['original_name'] = 'testString'
        object_meta_data_model['other'] = { 'foo': 'bar' }

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        overview_ui = overview_ui_model
        kind = 'testString'
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        group = True
        metadata = object_meta_data_model
        active = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "name": name,
            "overview_ui": overview_ui,
            "kind": kind,
            "images": images,
            "disabled": disabled,
            "tags": tags,
            "provider": provider,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_catalog_entry(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_catalog_entry
#-----------------------------------------------------------------------------
class TestGetCatalogEntry():

    #--------------------------------------------------------
    # get_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": []}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": []}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": []}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": []}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "metrics": []}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack"}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness"}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "compliance": ["compliance"], "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "kind": "kind", "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "active": true, "children": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        account = 'testString'
        include = 'testString'
        languages = 'testString'
        complete = 'testString'
        depth = 38

        # Invoke method
        response = service.get_catalog_entry(
            id,
            account=account,
            include=include,
            languages=languages,
            complete=complete,
            depth=depth,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'include={}'.format(include) in query_string
        assert 'languages={}'.format(languages) in query_string
        assert 'complete={}'.format(complete) in query_string
        assert 'depth={}'.format(depth) in query_string


    #--------------------------------------------------------
    # test_get_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": []}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": []}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": []}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": []}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "metrics": []}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack"}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness"}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "compliance": ["compliance"], "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "kind": "kind", "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "active": true, "children": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_catalog_entry(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/testString'
        mock_response = '{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": []}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": []}]}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid", "password": {"text": "text", "key": "key", "iv": "iv"}}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"strings": {}, "urls": {"doc_url": "doc_url", "instructions_url": "instructions_url", "api_url": "api_url", "create_url": "create_url", "sdk_download_url": "sdk_download_url", "terms_url": "terms_url", "custom_create_page_url": "custom_create_page_url", "catalog_details_url": "catalog_details_url", "deprecation_doc_url": "deprecation_doc_url"}, "embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": []}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": []}]}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "source": {"path": "path", "type": "type", "url": "url"}, "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack", "environment_variables": {"_key_": "key"}}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "broker": {"name": "name", "guid": "guid"}, "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness", "dr": {"dr": true, "description": "description"}}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "ui": {"embeddable_dashboard": "embeddable_dashboard", "embeddable_dashboard_full_width": false, "navigation_order": ["navigation_order"], "not_creatable": false, "reservable": true, "primary_offering_id": "primary_offering_id", "accessible_during_provision": false, "side_by_side_index": 18, "end_of_service_time": "2019-01-01T12:00:00"}, "pricing": {"type": "type", "origin": "origin", "metrics": []}, "compliance": ["compliance"], "service": {"type": "type", "iam_compatible": true, "unique_api_key": true, "provisionable": false, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "cf_guid": "cf_guid", "bindable": true, "requires": ["requires"], "plan_updateable": false, "state": "state", "service_check_enabled": false, "test_check_interval": 19, "service_key_supported": false}, "plan": {"bindable": true, "reservable": true, "allow_internal_users": true, "async_provisioning_supported": true, "async_unprovisioning_supported": true, "test_check_interval": 19, "single_scope_instance": "single_scope_instance", "service_check_enabled": false, "cf_guid": "cf_guid"}, "template": {"services": ["services"], "default_memory": 14, "start_cmd": "start_cmd", "runtime_catalog_id": "runtime_catalog_id", "cf_runtime_id": "cf_runtime_id", "template_id": "template_id", "executable_file": "executable_file", "buildpack": "buildpack"}, "deployment": {"location": "location", "location_url": "location_url", "target_crn": "target_crn", "supports_rc_migration": false}, "alias": {"type": "type", "plan_id": "plan_id"}, "sla": {"terms": "terms", "tenancy": "tenancy", "provisioning": "provisioning", "responsiveness": "responsiveness"}, "callbacks": {"broker_utl": "broker_utl", "broker_proxy_url": "broker_proxy_url", "dashboard_url": "dashboard_url", "dashboard_data_url": "dashboard_data_url", "dashboard_detail_tab_url": "dashboard_detail_tab_url", "dashboard_detail_tab_ext_url": "dashboard_detail_tab_ext_url", "service_monitor_api": "service_monitor_api", "service_monitor_app": "service_monitor_app", "service_staging_url": "service_staging_url", "service_production_url": "service_production_url"}, "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "overview_ui": {}, "kind": "kind", "images": {"image": "image", "small_image": "small_image", "medium_image": "medium_image", "feature_image": "feature_image"}, "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "provider": {"email": "email", "name": "name", "contact": "contact", "support_email": "support_email", "phone": "phone"}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "metadata": {"rc_compatible": false, "compliance": ["compliance"], "version": "version", "original_name": "original_name", "other": {"anyKey": "anyValue"}}, "active": true, "children": [{"id": "id", "catalog_crn": "catalog_crn", "url": "url", "name": "name", "kind": "kind", "parent_id": "parent_id", "children_url": "children_url", "parent_url": "parent_url", "disabled": true, "tags": ["tags"], "geo_tags": ["geo_tags"], "pricing_tags": ["pricing_tags"], "group": false, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "active": true, "children": []}]}]}]}]}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_catalog_entry(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_catalog_entry
#-----------------------------------------------------------------------------
class TestUpdateCatalogEntry():

    #--------------------------------------------------------
    # update_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['service_staging_url'] = 'testString'
        callbacks_model['service_production_url'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString'
        object_meta_data_alias_model['plan_id'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString'
        object_meta_data_deployment_model['target_crn'] = 'testString'
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model['supports_rc_migration'] = True

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True
        object_meta_data_plan_model['reservable'] = True
        object_meta_data_plan_model['allow_internal_users'] = True
        object_meta_data_plan_model['async_provisioning_supported'] = True
        object_meta_data_plan_model['async_unprovisioning_supported'] = True
        object_meta_data_plan_model['test_check_interval'] = 38
        object_meta_data_plan_model['single_scope_instance'] = 'testString'
        object_meta_data_plan_model['service_check_enabled'] = True
        object_meta_data_plan_model['cf_guid'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString'
        object_meta_data_service_model['iam_compatible'] = True
        object_meta_data_service_model['unique_api_key'] = True
        object_meta_data_service_model['provisionable'] = True
        object_meta_data_service_model['async_provisioning_supported'] = True
        object_meta_data_service_model['async_unprovisioning_supported'] = True
        object_meta_data_service_model['cf_guid'] = 'testString'
        object_meta_data_service_model['bindable'] = True
        object_meta_data_service_model['requires'] = ['testString']
        object_meta_data_service_model['plan_updateable'] = True
        object_meta_data_service_model['state'] = 'testString'
        object_meta_data_service_model['service_check_enabled'] = True
        object_meta_data_service_model['test_check_interval'] = 38
        object_meta_data_service_model['service_key_supported'] = True

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString'
        object_meta_data_sla_model['tenancy'] = 'testString'
        object_meta_data_sla_model['provisioning'] = 'testString'
        object_meta_data_sla_model['responsiveness'] = 'testString'
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString']
        object_meta_data_template_model['default_memory'] = 38
        object_meta_data_template_model['start_cmd'] = 'testString'
        object_meta_data_template_model['source'] = object_meta_data_template_source_model
        object_meta_data_template_model['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model['cf_runtime_id'] = 'testString'
        object_meta_data_template_model['template_id'] = 'testString'
        object_meta_data_template_model['executable_file'] = 'testString'
        object_meta_data_template_model['buildpack'] = 'testString'
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString'
        pricing_model['origin'] = 'testString'
        pricing_model['starting_price'] = starting_price_model
        pricing_model['metrics'] = [metrics_model]

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['reservable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True
        object_meta_data_model['ui'] = ui_meta_data_model
        object_meta_data_model['pricing'] = pricing_model
        object_meta_data_model['compliance'] = ['testString']
        object_meta_data_model['service'] = object_meta_data_service_model
        object_meta_data_model['plan'] = object_meta_data_plan_model
        object_meta_data_model['template'] = object_meta_data_template_model
        object_meta_data_model['deployment'] = object_meta_data_deployment_model
        object_meta_data_model['alias'] = object_meta_data_alias_model
        object_meta_data_model['sla'] = object_meta_data_sla_model
        object_meta_data_model['callbacks'] = callbacks_model
        object_meta_data_model['version'] = 'testString'
        object_meta_data_model['original_name'] = 'testString'
        object_meta_data_model['other'] = { 'foo': 'bar' }

        # Construct a dict representation of a CatalogEntry model
        catalog_entry_model = {}
        catalog_entry_model['name'] = 'testString'
        catalog_entry_model['overview_ui'] = overview_ui_model
        catalog_entry_model['kind'] = 'testString'
        catalog_entry_model['images'] = image_model
        catalog_entry_model['parent_id'] = 'testString'
        catalog_entry_model['parent_url'] = 'testString'
        catalog_entry_model['disabled'] = True
        catalog_entry_model['tags'] = ['testString']
        catalog_entry_model['group'] = True
        catalog_entry_model['provider'] = provider_model
        catalog_entry_model['metadata'] = object_meta_data_model
        catalog_entry_model['active'] = True

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        overview_ui = overview_ui_model
        kind = 'testString'
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        parent_url = 'testString'
        group = True
        metadata = object_meta_data_model
        active = True
        children = [catalog_entry_model]
        account = 'testString'
        move = 'testString'

        # Invoke method
        response = service.update_catalog_entry(
            id,
            name,
            overview_ui,
            kind,
            images,
            disabled,
            tags,
            provider,
            parent_id=parent_id,
            parent_url=parent_url,
            group=group,
            metadata=metadata,
            active=active,
            children=children,
            account=account,
            move=move,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'move={}'.format(move) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['overview_ui'] == overview_ui_model
        assert req_body['kind'] == 'testString'
        assert req_body['images'] == image_model
        assert req_body['disabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['provider'] == provider_model
        assert req_body['parent_id'] == 'testString'
        assert req_body['parent_url'] == 'testString'
        assert req_body['group'] == True
        assert req_body['metadata'] == object_meta_data_model
        assert req_body['active'] == True
        assert req_body['children'] == [catalog_entry_model]


    #--------------------------------------------------------
    # test_update_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['service_staging_url'] = 'testString'
        callbacks_model['service_production_url'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString'
        object_meta_data_alias_model['plan_id'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString'
        object_meta_data_deployment_model['target_crn'] = 'testString'
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model['supports_rc_migration'] = True

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True
        object_meta_data_plan_model['reservable'] = True
        object_meta_data_plan_model['allow_internal_users'] = True
        object_meta_data_plan_model['async_provisioning_supported'] = True
        object_meta_data_plan_model['async_unprovisioning_supported'] = True
        object_meta_data_plan_model['test_check_interval'] = 38
        object_meta_data_plan_model['single_scope_instance'] = 'testString'
        object_meta_data_plan_model['service_check_enabled'] = True
        object_meta_data_plan_model['cf_guid'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString'
        object_meta_data_service_model['iam_compatible'] = True
        object_meta_data_service_model['unique_api_key'] = True
        object_meta_data_service_model['provisionable'] = True
        object_meta_data_service_model['async_provisioning_supported'] = True
        object_meta_data_service_model['async_unprovisioning_supported'] = True
        object_meta_data_service_model['cf_guid'] = 'testString'
        object_meta_data_service_model['bindable'] = True
        object_meta_data_service_model['requires'] = ['testString']
        object_meta_data_service_model['plan_updateable'] = True
        object_meta_data_service_model['state'] = 'testString'
        object_meta_data_service_model['service_check_enabled'] = True
        object_meta_data_service_model['test_check_interval'] = 38
        object_meta_data_service_model['service_key_supported'] = True

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString'
        object_meta_data_sla_model['tenancy'] = 'testString'
        object_meta_data_sla_model['provisioning'] = 'testString'
        object_meta_data_sla_model['responsiveness'] = 'testString'
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString']
        object_meta_data_template_model['default_memory'] = 38
        object_meta_data_template_model['start_cmd'] = 'testString'
        object_meta_data_template_model['source'] = object_meta_data_template_source_model
        object_meta_data_template_model['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model['cf_runtime_id'] = 'testString'
        object_meta_data_template_model['template_id'] = 'testString'
        object_meta_data_template_model['executable_file'] = 'testString'
        object_meta_data_template_model['buildpack'] = 'testString'
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString'
        pricing_model['origin'] = 'testString'
        pricing_model['starting_price'] = starting_price_model
        pricing_model['metrics'] = [metrics_model]

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['reservable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True
        object_meta_data_model['ui'] = ui_meta_data_model
        object_meta_data_model['pricing'] = pricing_model
        object_meta_data_model['compliance'] = ['testString']
        object_meta_data_model['service'] = object_meta_data_service_model
        object_meta_data_model['plan'] = object_meta_data_plan_model
        object_meta_data_model['template'] = object_meta_data_template_model
        object_meta_data_model['deployment'] = object_meta_data_deployment_model
        object_meta_data_model['alias'] = object_meta_data_alias_model
        object_meta_data_model['sla'] = object_meta_data_sla_model
        object_meta_data_model['callbacks'] = callbacks_model
        object_meta_data_model['version'] = 'testString'
        object_meta_data_model['original_name'] = 'testString'
        object_meta_data_model['other'] = { 'foo': 'bar' }

        # Construct a dict representation of a CatalogEntry model
        catalog_entry_model = {}
        catalog_entry_model['name'] = 'testString'
        catalog_entry_model['overview_ui'] = overview_ui_model
        catalog_entry_model['kind'] = 'testString'
        catalog_entry_model['images'] = image_model
        catalog_entry_model['parent_id'] = 'testString'
        catalog_entry_model['parent_url'] = 'testString'
        catalog_entry_model['disabled'] = True
        catalog_entry_model['tags'] = ['testString']
        catalog_entry_model['group'] = True
        catalog_entry_model['provider'] = provider_model
        catalog_entry_model['metadata'] = object_meta_data_model
        catalog_entry_model['active'] = True

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        overview_ui = overview_ui_model
        kind = 'testString'
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        parent_url = 'testString'
        group = True
        metadata = object_meta_data_model
        active = True
        children = [catalog_entry_model]

        # Invoke method
        response = service.update_catalog_entry(
            id,
            name,
            overview_ui,
            kind,
            images,
            disabled,
            tags,
            provider,
            parent_id=parent_id,
            parent_url=parent_url,
            group=group,
            metadata=metadata,
            active=active,
            children=children,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['overview_ui'] == overview_ui_model
        assert req_body['kind'] == 'testString'
        assert req_body['images'] == image_model
        assert req_body['disabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['provider'] == provider_model
        assert req_body['parent_id'] == 'testString'
        assert req_body['parent_url'] == 'testString'
        assert req_body['group'] == True
        assert req_body['metadata'] == object_meta_data_model
        assert req_body['active'] == True
        assert req_body['children'] == [catalog_entry_model]


    #--------------------------------------------------------
    # test_update_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'

        # Construct a dict representation of a OverviewUI model
        overview_ui_model = {}
        overview_ui_model['foo'] = overview_model

        # Construct a dict representation of a Image model
        image_model = {}
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        # Construct a dict representation of a Provider model
        provider_model = {}
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a dict representation of a Bullets model
        bullets_model = {}
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        # Construct a dict representation of a Price model
        price_model = {}
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a dict representation of a UIMetaMedia model
        ui_meta_media_model = {}
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a dict representation of a Amount model
        amount_model = {}
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model = {}
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        # Construct a dict representation of a Strings model
        strings_model = {}
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a dict representation of a I18N model
        i18_n_model = {}
        i18_n_model['foo'] = strings_model

        # Construct a dict representation of a Metrics model
        metrics_model = {}
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        # Construct a dict representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model = {}
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        # Construct a dict representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model = {}
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model = {}
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model = {}
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        # Construct a dict representation of a StartingPrice model
        starting_price_model = {}
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a dict representation of a URLS model
        urls_model = {}
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        # Construct a dict representation of a Callbacks model
        callbacks_model = {}
        callbacks_model['broker_utl'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['service_staging_url'] = 'testString'
        callbacks_model['service_production_url'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model = {}
        object_meta_data_alias_model['type'] = 'testString'
        object_meta_data_alias_model['plan_id'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model = {}
        object_meta_data_deployment_model['location'] = 'testString'
        object_meta_data_deployment_model['target_crn'] = 'testString'
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model['supports_rc_migration'] = True

        # Construct a dict representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model = {}
        object_meta_data_plan_model['bindable'] = True
        object_meta_data_plan_model['reservable'] = True
        object_meta_data_plan_model['allow_internal_users'] = True
        object_meta_data_plan_model['async_provisioning_supported'] = True
        object_meta_data_plan_model['async_unprovisioning_supported'] = True
        object_meta_data_plan_model['test_check_interval'] = 38
        object_meta_data_plan_model['single_scope_instance'] = 'testString'
        object_meta_data_plan_model['service_check_enabled'] = True
        object_meta_data_plan_model['cf_guid'] = 'testString'

        # Construct a dict representation of a ObjectMetaDataService model
        object_meta_data_service_model = {}
        object_meta_data_service_model['type'] = 'testString'
        object_meta_data_service_model['iam_compatible'] = True
        object_meta_data_service_model['unique_api_key'] = True
        object_meta_data_service_model['provisionable'] = True
        object_meta_data_service_model['async_provisioning_supported'] = True
        object_meta_data_service_model['async_unprovisioning_supported'] = True
        object_meta_data_service_model['cf_guid'] = 'testString'
        object_meta_data_service_model['bindable'] = True
        object_meta_data_service_model['requires'] = ['testString']
        object_meta_data_service_model['plan_updateable'] = True
        object_meta_data_service_model['state'] = 'testString'
        object_meta_data_service_model['service_check_enabled'] = True
        object_meta_data_service_model['test_check_interval'] = 38
        object_meta_data_service_model['service_key_supported'] = True

        # Construct a dict representation of a ObjectMetaDataSla model
        object_meta_data_sla_model = {}
        object_meta_data_sla_model['terms'] = 'testString'
        object_meta_data_sla_model['tenancy'] = 'testString'
        object_meta_data_sla_model['provisioning'] = 'testString'
        object_meta_data_sla_model['responsiveness'] = 'testString'
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model

        # Construct a dict representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model = {}
        object_meta_data_template_model['services'] = ['testString']
        object_meta_data_template_model['default_memory'] = 38
        object_meta_data_template_model['start_cmd'] = 'testString'
        object_meta_data_template_model['source'] = object_meta_data_template_source_model
        object_meta_data_template_model['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model['cf_runtime_id'] = 'testString'
        object_meta_data_template_model['template_id'] = 'testString'
        object_meta_data_template_model['executable_file'] = 'testString'
        object_meta_data_template_model['buildpack'] = 'testString'
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['type'] = 'testString'
        pricing_model['origin'] = 'testString'
        pricing_model['starting_price'] = starting_price_model
        pricing_model['metrics'] = [metrics_model]

        # Construct a dict representation of a UIMetaData model
        ui_meta_data_model = {}
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['reservable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ObjectMetaData model
        object_meta_data_model = {}
        object_meta_data_model['rc_compatible'] = True
        object_meta_data_model['ui'] = ui_meta_data_model
        object_meta_data_model['pricing'] = pricing_model
        object_meta_data_model['compliance'] = ['testString']
        object_meta_data_model['service'] = object_meta_data_service_model
        object_meta_data_model['plan'] = object_meta_data_plan_model
        object_meta_data_model['template'] = object_meta_data_template_model
        object_meta_data_model['deployment'] = object_meta_data_deployment_model
        object_meta_data_model['alias'] = object_meta_data_alias_model
        object_meta_data_model['sla'] = object_meta_data_sla_model
        object_meta_data_model['callbacks'] = callbacks_model
        object_meta_data_model['version'] = 'testString'
        object_meta_data_model['original_name'] = 'testString'
        object_meta_data_model['other'] = { 'foo': 'bar' }

        # Construct a dict representation of a CatalogEntry model
        catalog_entry_model = {}
        catalog_entry_model['name'] = 'testString'
        catalog_entry_model['overview_ui'] = overview_ui_model
        catalog_entry_model['kind'] = 'testString'
        catalog_entry_model['images'] = image_model
        catalog_entry_model['parent_id'] = 'testString'
        catalog_entry_model['parent_url'] = 'testString'
        catalog_entry_model['disabled'] = True
        catalog_entry_model['tags'] = ['testString']
        catalog_entry_model['group'] = True
        catalog_entry_model['provider'] = provider_model
        catalog_entry_model['metadata'] = object_meta_data_model
        catalog_entry_model['active'] = True

        # Set up parameter values
        id = 'testString'
        name = 'testString'
        overview_ui = overview_ui_model
        kind = 'testString'
        images = image_model
        disabled = True
        tags = ['testString']
        provider = provider_model
        parent_id = 'testString'
        parent_url = 'testString'
        group = True
        metadata = object_meta_data_model
        active = True
        children = [catalog_entry_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "name": name,
            "overview_ui": overview_ui,
            "kind": kind,
            "images": images,
            "disabled": disabled,
            "tags": tags,
            "provider": provider,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_catalog_entry(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_catalog_entry
#-----------------------------------------------------------------------------
class TestDeleteCatalogEntry():

    #--------------------------------------------------------
    # delete_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.delete_catalog_entry(
            id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_delete_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_catalog_entry(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_catalog_entry(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_child_objects
#-----------------------------------------------------------------------------
class TestGetChildObjects():

    #--------------------------------------------------------
    # get_child_objects()
    #--------------------------------------------------------
    @responses.activate
    def test_get_child_objects_all_params(self):
        # Set up mock
        url = base_url + '/testString/testString'
        mock_response = '[{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        kind = 'testString'
        account = 'testString'
        include = 'testString'
        q = 'testString'
        sort_by = 'testString'
        descending = 'testString'
        languages = 'testString'
        complete = 'testString'

        # Invoke method
        response = service.get_child_objects(
            id,
            kind,
            account=account,
            include=include,
            q=q,
            sort_by=sort_by,
            descending=descending,
            languages=languages,
            complete=complete,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'include={}'.format(include) in query_string
        assert 'q={}'.format(q) in query_string
        assert 'sort-by={}'.format(sort_by) in query_string
        assert 'descending={}'.format(descending) in query_string
        assert 'languages={}'.format(languages) in query_string
        assert 'complete={}'.format(complete) in query_string


    #--------------------------------------------------------
    # test_get_child_objects_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_child_objects_required_params(self):
        # Set up mock
        url = base_url + '/testString/testString'
        mock_response = '[{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        kind = 'testString'

        # Invoke method
        response = service.get_child_objects(
            id,
            kind,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_child_objects_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_child_objects_value_error(self):
        # Set up mock
        url = base_url + '/testString/testString'
        mock_response = '[{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        kind = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "kind": kind,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_child_objects(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for restore_catalog_entry
#-----------------------------------------------------------------------------
class TestRestoreCatalogEntry():

    #--------------------------------------------------------
    # restore_catalog_entry()
    #--------------------------------------------------------
    @responses.activate
    def test_restore_catalog_entry_all_params(self):
        # Set up mock
        url = base_url + '/testString/restore'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.restore_catalog_entry(
            id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_restore_catalog_entry_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_restore_catalog_entry_required_params(self):
        # Set up mock
        url = base_url + '/testString/restore'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.restore_catalog_entry(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_restore_catalog_entry_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_restore_catalog_entry_value_error(self):
        # Set up mock
        url = base_url + '/testString/restore'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.restore_catalog_entry(**req_copy)



# endregion
##############################################################################
# End of Service: Object
##############################################################################

##############################################################################
# Start of Service: Visibility
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_visibility
#-----------------------------------------------------------------------------
class TestGetVisibility():

    #--------------------------------------------------------
    # get_visibility()
    #--------------------------------------------------------
    @responses.activate
    def test_get_visibility_all_params(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        mock_response = '{"restrictions": "restrictions", "owner": {"type": "type", "value": "value"}, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.get_visibility(
            id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_get_visibility_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_visibility_required_params(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        mock_response = '{"restrictions": "restrictions", "owner": {"type": "type", "value": "value"}, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_visibility(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_visibility_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_visibility_value_error(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        mock_response = '{"restrictions": "restrictions", "owner": {"type": "type", "value": "value"}, "include": {"accounts": {"_accountid_": "accountid"}}, "exclude": {"accounts": {"_accountid_": "accountid"}}, "approved": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_visibility(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_visibility
#-----------------------------------------------------------------------------
class TestUpdateVisibility():

    #--------------------------------------------------------
    # update_visibility()
    #--------------------------------------------------------
    @responses.activate
    def test_update_visibility_all_params(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a Scope model
        scope_model = {}
        scope_model['type'] = 'testString'
        scope_model['value'] = 'testString'

        # Construct a dict representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model = {}
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        # Construct a dict representation of a VisibilityDetail model
        visibility_detail_model = {}
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        # Set up parameter values
        id = 'testString'
        owner = scope_model
        include = visibility_detail_model
        exclude = visibility_detail_model
        account = 'testString'

        # Invoke method
        response = service.update_visibility(
            id,
            owner=owner,
            include=include,
            exclude=exclude,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['owner'] == scope_model
        assert req_body['include'] == visibility_detail_model
        assert req_body['exclude'] == visibility_detail_model


    #--------------------------------------------------------
    # test_update_visibility_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_visibility_required_params(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a Scope model
        scope_model = {}
        scope_model['type'] = 'testString'
        scope_model['value'] = 'testString'

        # Construct a dict representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model = {}
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        # Construct a dict representation of a VisibilityDetail model
        visibility_detail_model = {}
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        # Set up parameter values
        id = 'testString'
        owner = scope_model
        include = visibility_detail_model
        exclude = visibility_detail_model

        # Invoke method
        response = service.update_visibility(
            id,
            owner=owner,
            include=include,
            exclude=exclude,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['owner'] == scope_model
        assert req_body['include'] == visibility_detail_model
        assert req_body['exclude'] == visibility_detail_model


    #--------------------------------------------------------
    # test_update_visibility_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_visibility_value_error(self):
        # Set up mock
        url = base_url + '/testString/visibility'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a Scope model
        scope_model = {}
        scope_model['type'] = 'testString'
        scope_model['value'] = 'testString'

        # Construct a dict representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model = {}
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        # Construct a dict representation of a VisibilityDetail model
        visibility_detail_model = {}
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        # Set up parameter values
        id = 'testString'
        owner = scope_model
        include = visibility_detail_model
        exclude = visibility_detail_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_visibility(**req_copy)



# endregion
##############################################################################
# End of Service: Visibility
##############################################################################

##############################################################################
# Start of Service: Pricing
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_pricing
#-----------------------------------------------------------------------------
class TestGetPricing():

    #--------------------------------------------------------
    # get_pricing()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pricing_all_params(self):
        # Set up mock
        url = base_url + '/testString/pricing'
        mock_response = '{"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.get_pricing(
            id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_get_pricing_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pricing_required_params(self):
        # Set up mock
        url = base_url + '/testString/pricing'
        mock_response = '{"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_pricing(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_pricing_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pricing_value_error(self):
        # Set up mock
        url = base_url + '/testString/pricing'
        mock_response = '{"type": "type", "origin": "origin", "starting_price": {"plan_id": "plan_id", "deployment_id": "deployment_id", "amount": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}, "metrics": [{"metric_id": "metric_id", "tier_model": "tier_model", "charge_unit_name": "charge_unit_name", "charge_unit_quantity": "charge_unit_quantity", "resource_display_name": "resource_display_name", "charge_unit_display_name": "charge_unit_display_name", "usage_cap_qty": 13, "amounts": [{"counrty": "counrty", "currency": "currency", "prices": [{"quantity_tier": 13, "Price": 5}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_pricing(**req_copy)



# endregion
##############################################################################
# End of Service: Pricing
##############################################################################

##############################################################################
# Start of Service: Audit
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_audit_logs
#-----------------------------------------------------------------------------
class TestGetAuditLogs():

    #--------------------------------------------------------
    # get_audit_logs()
    #--------------------------------------------------------
    @responses.activate
    def test_get_audit_logs_all_params(self):
        # Set up mock
        url = base_url + '/testString/logs'
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        account = 'testString'
        ascending = 'testString'
        startat = 'testString'
        offset = 38
        limit = 38

        # Invoke method
        response = service.get_audit_logs(
            id,
            account=account,
            ascending=ascending,
            startat=startat,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string
        assert 'ascending={}'.format(ascending) in query_string
        assert 'startat={}'.format(startat) in query_string
        assert '_offset={}'.format(offset) in query_string
        assert '_limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_get_audit_logs_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_audit_logs_required_params(self):
        # Set up mock
        url = base_url + '/testString/logs'
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_audit_logs(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_audit_logs_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_audit_logs_value_error(self):
        # Set up mock
        url = base_url + '/testString/logs'
        mock_response = '{"page": "page", "results_per_page": "results_per_page", "total_results": "total_results", "resources": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_audit_logs(**req_copy)



# endregion
##############################################################################
# End of Service: Audit
##############################################################################

##############################################################################
# Start of Service: Artifact
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_artifacts
#-----------------------------------------------------------------------------
class TestListArtifacts():

    #--------------------------------------------------------
    # list_artifacts()
    #--------------------------------------------------------
    @responses.activate
    def test_list_artifacts_all_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts'
        mock_response = '{"count": 5, "resources": [{"name": "name", "updated": "updated", "url": "url", "etag": "etag", "size": 4}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.list_artifacts(
            object_id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_list_artifacts_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_artifacts_required_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts'
        mock_response = '{"count": 5, "resources": [{"name": "name", "updated": "updated", "url": "url", "etag": "etag", "size": 4}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        object_id = 'testString'

        # Invoke method
        response = service.list_artifacts(
            object_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_artifacts_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_artifacts_value_error(self):
        # Set up mock
        url = base_url + '/testString/artifacts'
        mock_response = '{"count": 5, "resources": [{"name": "name", "updated": "updated", "url": "url", "etag": "etag", "size": 4}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        object_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "object_id": object_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_artifacts(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_artifact
#-----------------------------------------------------------------------------
class TestGetArtifact():

    #--------------------------------------------------------
    # get_artifact()
    #--------------------------------------------------------
    @responses.activate
    def test_get_artifact_all_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.get_artifact(
            object_id,
            artifact_id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_get_artifact_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_artifact_required_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Invoke method
        response = service.get_artifact(
            object_id,
            artifact_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_artifact_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_artifact_value_error(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "object_id": object_id,
            "artifact_id": artifact_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_artifact(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for upload_artifact
#-----------------------------------------------------------------------------
class TestUploadArtifact():

    #--------------------------------------------------------
    # upload_artifact()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_artifact_all_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.upload_artifact(
            object_id,
            artifact_id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_upload_artifact_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_artifact_required_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Invoke method
        response = service.upload_artifact(
            object_id,
            artifact_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_upload_artifact_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_artifact_value_error(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "object_id": object_id,
            "artifact_id": artifact_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.upload_artifact(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_artifact
#-----------------------------------------------------------------------------
class TestDeleteArtifact():

    #--------------------------------------------------------
    # delete_artifact()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_artifact_all_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'
        account = 'testString'

        # Invoke method
        response = service.delete_artifact(
            object_id,
            artifact_id,
            account=account,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account={}'.format(account) in query_string


    #--------------------------------------------------------
    # test_delete_artifact_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_artifact_required_params(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Invoke method
        response = service.delete_artifact(
            object_id,
            artifact_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_artifact_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_artifact_value_error(self):
        # Set up mock
        url = base_url + '/testString/artifacts/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        object_id = 'testString'
        artifact_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "object_id": object_id,
            "artifact_id": artifact_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_artifact(**req_copy)



# endregion
##############################################################################
# End of Service: Artifact
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for Amount
#-----------------------------------------------------------------------------
class TestAmount():

    #--------------------------------------------------------
    # Test serialization/deserialization for Amount
    #--------------------------------------------------------
    def test_amount_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        # Construct a json representation of a Amount model
        amount_model_json = {}
        amount_model_json['counrty'] = 'testString'
        amount_model_json['currency'] = 'testString'
        amount_model_json['prices'] = [price_model]

        # Construct a model instance of Amount by calling from_dict on the json representation
        amount_model = Amount.from_dict(amount_model_json)
        assert amount_model != False

        # Construct a model instance of Amount by calling from_dict on the json representation
        amount_model_dict = Amount.from_dict(amount_model_json).__dict__
        amount_model2 = Amount(**amount_model_dict)

        # Verify the model instances are equivalent
        assert amount_model == amount_model2

        # Convert model instance back to dict and verify no loss of data
        amount_model_json2 = amount_model.to_dict()
        assert amount_model_json2 == amount_model_json

#-----------------------------------------------------------------------------
# Test Class for Artifact
#-----------------------------------------------------------------------------
class TestArtifact():

    #--------------------------------------------------------
    # Test serialization/deserialization for Artifact
    #--------------------------------------------------------
    def test_artifact_serialization(self):

        # Construct a json representation of a Artifact model
        artifact_model_json = {}
        artifact_model_json['name'] = 'testString'
        artifact_model_json['updated'] = 'testString'
        artifact_model_json['url'] = 'testString'
        artifact_model_json['etag'] = 'testString'
        artifact_model_json['size'] = 38

        # Construct a model instance of Artifact by calling from_dict on the json representation
        artifact_model = Artifact.from_dict(artifact_model_json)
        assert artifact_model != False

        # Construct a model instance of Artifact by calling from_dict on the json representation
        artifact_model_dict = Artifact.from_dict(artifact_model_json).__dict__
        artifact_model2 = Artifact(**artifact_model_dict)

        # Verify the model instances are equivalent
        assert artifact_model == artifact_model2

        # Convert model instance back to dict and verify no loss of data
        artifact_model_json2 = artifact_model.to_dict()
        assert artifact_model_json2 == artifact_model_json

#-----------------------------------------------------------------------------
# Test Class for Artifacts
#-----------------------------------------------------------------------------
class TestArtifacts():

    #--------------------------------------------------------
    # Test serialization/deserialization for Artifacts
    #--------------------------------------------------------
    def test_artifacts_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        artifact_model = {} # Artifact
        artifact_model['name'] = 'testString'
        artifact_model['updated'] = 'testString'
        artifact_model['url'] = 'testString'
        artifact_model['etag'] = 'testString'
        artifact_model['size'] = 38

        # Construct a json representation of a Artifacts model
        artifacts_model_json = {}
        artifacts_model_json['count'] = 38
        artifacts_model_json['resources'] = [artifact_model]

        # Construct a model instance of Artifacts by calling from_dict on the json representation
        artifacts_model = Artifacts.from_dict(artifacts_model_json)
        assert artifacts_model != False

        # Construct a model instance of Artifacts by calling from_dict on the json representation
        artifacts_model_dict = Artifacts.from_dict(artifacts_model_json).__dict__
        artifacts_model2 = Artifacts(**artifacts_model_dict)

        # Verify the model instances are equivalent
        assert artifacts_model == artifacts_model2

        # Convert model instance back to dict and verify no loss of data
        artifacts_model_json2 = artifacts_model.to_dict()
        assert artifacts_model_json2 == artifacts_model_json

#-----------------------------------------------------------------------------
# Test Class for Bullets
#-----------------------------------------------------------------------------
class TestBullets():

    #--------------------------------------------------------
    # Test serialization/deserialization for Bullets
    #--------------------------------------------------------
    def test_bullets_serialization(self):

        # Construct a json representation of a Bullets model
        bullets_model_json = {}
        bullets_model_json['title'] = 'testString'
        bullets_model_json['description'] = 'testString'
        bullets_model_json['icon'] = 'testString'
        bullets_model_json['quantity'] = 'testString'

        # Construct a model instance of Bullets by calling from_dict on the json representation
        bullets_model = Bullets.from_dict(bullets_model_json)
        assert bullets_model != False

        # Construct a model instance of Bullets by calling from_dict on the json representation
        bullets_model_dict = Bullets.from_dict(bullets_model_json).__dict__
        bullets_model2 = Bullets(**bullets_model_dict)

        # Verify the model instances are equivalent
        assert bullets_model == bullets_model2

        # Convert model instance back to dict and verify no loss of data
        bullets_model_json2 = bullets_model.to_dict()
        assert bullets_model_json2 == bullets_model_json

#-----------------------------------------------------------------------------
# Test Class for Callbacks
#-----------------------------------------------------------------------------
class TestCallbacks():

    #--------------------------------------------------------
    # Test serialization/deserialization for Callbacks
    #--------------------------------------------------------
    def test_callbacks_serialization(self):

        # Construct a json representation of a Callbacks model
        callbacks_model_json = {}
        callbacks_model_json['broker_utl'] = 'testString'
        callbacks_model_json['broker_proxy_url'] = 'testString'
        callbacks_model_json['dashboard_url'] = 'testString'
        callbacks_model_json['dashboard_data_url'] = 'testString'
        callbacks_model_json['dashboard_detail_tab_url'] = 'testString'
        callbacks_model_json['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model_json['service_monitor_api'] = 'testString'
        callbacks_model_json['service_monitor_app'] = 'testString'
        callbacks_model_json['service_staging_url'] = 'testString'
        callbacks_model_json['service_production_url'] = 'testString'

        # Construct a model instance of Callbacks by calling from_dict on the json representation
        callbacks_model = Callbacks.from_dict(callbacks_model_json)
        assert callbacks_model != False

        # Construct a model instance of Callbacks by calling from_dict on the json representation
        callbacks_model_dict = Callbacks.from_dict(callbacks_model_json).__dict__
        callbacks_model2 = Callbacks(**callbacks_model_dict)

        # Verify the model instances are equivalent
        assert callbacks_model == callbacks_model2

        # Convert model instance back to dict and verify no loss of data
        callbacks_model_json2 = callbacks_model.to_dict()
        assert callbacks_model_json2 == callbacks_model_json

#-----------------------------------------------------------------------------
# Test Class for CatalogEntry
#-----------------------------------------------------------------------------
class TestCatalogEntry():

    #--------------------------------------------------------
    # Test serialization/deserialization for CatalogEntry
    #--------------------------------------------------------
    def test_catalog_entry_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        amount_model = {} # Amount
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        object_meta_data_deployment_broker_password_model = {} # ObjectMetaDataDeploymentBrokerPassword
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        i18_n_model = {} # I18N
        i18_n_model['foo'] = strings_model

        metrics_model = {} # Metrics
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        object_meta_data_deployment_broker_model = {} # ObjectMetaDataDeploymentBroker
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        object_meta_data_sla_dr_model = {} # ObjectMetaDataSlaDr
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        object_meta_data_template_environment_variables_model = {} # ObjectMetaDataTemplateEnvironmentVariables
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        object_meta_data_template_source_model = {} # ObjectMetaDataTemplateSource
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        urls_model = {} # URLS
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        callbacks_model = {} # Callbacks
        callbacks_model['broker_utl'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['service_staging_url'] = 'testString'
        callbacks_model['service_production_url'] = 'testString'

        object_meta_data_alias_model = {} # ObjectMetaDataAlias
        object_meta_data_alias_model['type'] = 'testString'
        object_meta_data_alias_model['plan_id'] = 'testString'

        object_meta_data_deployment_model = {} # ObjectMetaDataDeployment
        object_meta_data_deployment_model['location'] = 'testString'
        object_meta_data_deployment_model['location_url'] = 'testString'
        object_meta_data_deployment_model['target_crn'] = 'testString'
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model['supports_rc_migration'] = True

        object_meta_data_plan_model = {} # ObjectMetaDataPlan
        object_meta_data_plan_model['bindable'] = True
        object_meta_data_plan_model['reservable'] = True
        object_meta_data_plan_model['allow_internal_users'] = True
        object_meta_data_plan_model['async_provisioning_supported'] = True
        object_meta_data_plan_model['async_unprovisioning_supported'] = True
        object_meta_data_plan_model['test_check_interval'] = 38
        object_meta_data_plan_model['single_scope_instance'] = 'testString'
        object_meta_data_plan_model['service_check_enabled'] = True
        object_meta_data_plan_model['cf_guid'] = 'testString'

        object_meta_data_service_model = {} # ObjectMetaDataService
        object_meta_data_service_model['type'] = 'testString'
        object_meta_data_service_model['iam_compatible'] = True
        object_meta_data_service_model['unique_api_key'] = True
        object_meta_data_service_model['provisionable'] = True
        object_meta_data_service_model['async_provisioning_supported'] = True
        object_meta_data_service_model['async_unprovisioning_supported'] = True
        object_meta_data_service_model['cf_guid'] = 'testString'
        object_meta_data_service_model['bindable'] = True
        object_meta_data_service_model['requires'] = ['testString']
        object_meta_data_service_model['plan_updateable'] = True
        object_meta_data_service_model['state'] = 'testString'
        object_meta_data_service_model['service_check_enabled'] = True
        object_meta_data_service_model['test_check_interval'] = 38
        object_meta_data_service_model['service_key_supported'] = True

        object_meta_data_sla_model = {} # ObjectMetaDataSla
        object_meta_data_sla_model['terms'] = 'testString'
        object_meta_data_sla_model['tenancy'] = 'testString'
        object_meta_data_sla_model['provisioning'] = 'testString'
        object_meta_data_sla_model['responsiveness'] = 'testString'
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model

        object_meta_data_template_model = {} # ObjectMetaDataTemplate
        object_meta_data_template_model['services'] = ['testString']
        object_meta_data_template_model['default_memory'] = 38
        object_meta_data_template_model['start_cmd'] = 'testString'
        object_meta_data_template_model['source'] = object_meta_data_template_source_model
        object_meta_data_template_model['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model['cf_runtime_id'] = 'testString'
        object_meta_data_template_model['template_id'] = 'testString'
        object_meta_data_template_model['executable_file'] = 'testString'
        object_meta_data_template_model['buildpack'] = 'testString'
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model

        overview_model = {} # Overview
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'

        pricing_model = {} # Pricing
        pricing_model['type'] = 'testString'
        pricing_model['origin'] = 'testString'
        pricing_model['starting_price'] = starting_price_model
        pricing_model['metrics'] = [metrics_model]

        ui_meta_data_model = {} # UIMetaData
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['reservable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        image_model = {} # Image
        image_model['image'] = 'testString'
        image_model['small_image'] = 'testString'
        image_model['medium_image'] = 'testString'
        image_model['feature_image'] = 'testString'

        object_meta_data_model = {} # ObjectMetaData
        object_meta_data_model['rc_compatible'] = True
        object_meta_data_model['ui'] = ui_meta_data_model
        object_meta_data_model['pricing'] = pricing_model
        object_meta_data_model['compliance'] = ['testString']
        object_meta_data_model['service'] = object_meta_data_service_model
        object_meta_data_model['plan'] = object_meta_data_plan_model
        object_meta_data_model['template'] = object_meta_data_template_model
        object_meta_data_model['deployment'] = object_meta_data_deployment_model
        object_meta_data_model['alias'] = object_meta_data_alias_model
        object_meta_data_model['sla'] = object_meta_data_sla_model
        object_meta_data_model['callbacks'] = callbacks_model
        object_meta_data_model['version'] = 'testString'
        object_meta_data_model['original_name'] = 'testString'
        object_meta_data_model['other'] = { 'foo': 'bar' }

        overview_ui_model = {} # OverviewUI
        overview_ui_model['foo'] = overview_model

        provider_model = {} # Provider
        provider_model['email'] = 'testString'
        provider_model['name'] = 'testString'
        provider_model['contact'] = 'testString'
        provider_model['support_email'] = 'testString'
        provider_model['phone'] = 'testString'

        # Construct a json representation of a CatalogEntry model
        catalog_entry_model_json = {}
        catalog_entry_model_json['id'] = 'testString'
        catalog_entry_model_json['catalog_crn'] = 'testString'
        catalog_entry_model_json['url'] = 'testString'
        catalog_entry_model_json['name'] = 'testString'
        catalog_entry_model_json['overview_ui'] = overview_ui_model
        catalog_entry_model_json['kind'] = 'testString'
        catalog_entry_model_json['images'] = image_model
        catalog_entry_model_json['parent_id'] = 'testString'
        catalog_entry_model_json['children_url'] = 'testString'
        catalog_entry_model_json['parent_url'] = 'testString'
        catalog_entry_model_json['disabled'] = True
        catalog_entry_model_json['tags'] = ['testString']
        catalog_entry_model_json['geo_tags'] = ['testString']
        catalog_entry_model_json['pricing_tags'] = ['testString']
        catalog_entry_model_json['group'] = True
        catalog_entry_model_json['provider'] = provider_model
        catalog_entry_model_json['created'] = '2020-01-28T18:40:40.123456Z'
        catalog_entry_model_json['updated'] = '2020-01-28T18:40:40.123456Z'
        catalog_entry_model_json['metadata'] = object_meta_data_model
        catalog_entry_model_json['active'] = True

        # Construct a model instance of CatalogEntry by calling from_dict on the json representation
        catalog_entry_model = CatalogEntry.from_dict(catalog_entry_model_json)
        assert catalog_entry_model != False

        # Construct a model instance of CatalogEntry by calling from_dict on the json representation
        catalog_entry_model_dict = CatalogEntry.from_dict(catalog_entry_model_json).__dict__
        catalog_entry_model2 = CatalogEntry(**catalog_entry_model_dict)

        # Verify the model instances are equivalent
        assert catalog_entry_model == catalog_entry_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_entry_model_json2 = catalog_entry_model.to_dict()
        assert catalog_entry_model_json2 == catalog_entry_model_json

#-----------------------------------------------------------------------------
# Test Class for I18N
#-----------------------------------------------------------------------------
class TestI18N():

    #--------------------------------------------------------
    # Test serialization/deserialization for I18N
    #--------------------------------------------------------
    def test_i18_n_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        # Construct a json representation of a I18N model
        i18_n_model_json = {}
        i18_n_model_json['foo'] = strings_model

        # Construct a model instance of I18N by calling from_dict on the json representation
        i18_n_model = I18N.from_dict(i18_n_model_json)
        assert i18_n_model != False

        # Construct a model instance of I18N by calling from_dict on the json representation
        i18_n_model_dict = I18N.from_dict(i18_n_model_json).__dict__
        i18_n_model2 = I18N(**i18_n_model_dict)

        # Verify the model instances are equivalent
        assert i18_n_model == i18_n_model2

        # Convert model instance back to dict and verify no loss of data
        i18_n_model_json2 = i18_n_model.to_dict()
        assert i18_n_model_json2 == i18_n_model_json

#-----------------------------------------------------------------------------
# Test Class for Image
#-----------------------------------------------------------------------------
class TestImage():

    #--------------------------------------------------------
    # Test serialization/deserialization for Image
    #--------------------------------------------------------
    def test_image_serialization(self):

        # Construct a json representation of a Image model
        image_model_json = {}
        image_model_json['image'] = 'testString'
        image_model_json['small_image'] = 'testString'
        image_model_json['medium_image'] = 'testString'
        image_model_json['feature_image'] = 'testString'

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model = Image.from_dict(image_model_json)
        assert image_model != False

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model_dict = Image.from_dict(image_model_json).__dict__
        image_model2 = Image(**image_model_dict)

        # Verify the model instances are equivalent
        assert image_model == image_model2

        # Convert model instance back to dict and verify no loss of data
        image_model_json2 = image_model.to_dict()
        assert image_model_json2 == image_model_json

#-----------------------------------------------------------------------------
# Test Class for Metrics
#-----------------------------------------------------------------------------
class TestMetrics():

    #--------------------------------------------------------
    # Test serialization/deserialization for Metrics
    #--------------------------------------------------------
    def test_metrics_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        amount_model = {} # Amount
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a json representation of a Metrics model
        metrics_model_json = {}
        metrics_model_json['metric_id'] = 'testString'
        metrics_model_json['tier_model'] = 'testString'
        metrics_model_json['charge_unit_name'] = 'testString'
        metrics_model_json['charge_unit_quantity'] = 'testString'
        metrics_model_json['resource_display_name'] = 'testString'
        metrics_model_json['charge_unit_display_name'] = 'testString'
        metrics_model_json['usage_cap_qty'] = 38
        metrics_model_json['amounts'] = [amount_model]

        # Construct a model instance of Metrics by calling from_dict on the json representation
        metrics_model = Metrics.from_dict(metrics_model_json)
        assert metrics_model != False

        # Construct a model instance of Metrics by calling from_dict on the json representation
        metrics_model_dict = Metrics.from_dict(metrics_model_json).__dict__
        metrics_model2 = Metrics(**metrics_model_dict)

        # Verify the model instances are equivalent
        assert metrics_model == metrics_model2

        # Convert model instance back to dict and verify no loss of data
        metrics_model_json2 = metrics_model.to_dict()
        assert metrics_model_json2 == metrics_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaData
#-----------------------------------------------------------------------------
class TestObjectMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaData
    #--------------------------------------------------------
    def test_object_meta_data_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        amount_model = {} # Amount
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        object_meta_data_deployment_broker_password_model = {} # ObjectMetaDataDeploymentBrokerPassword
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        i18_n_model = {} # I18N
        i18_n_model['foo'] = strings_model

        metrics_model = {} # Metrics
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        object_meta_data_deployment_broker_model = {} # ObjectMetaDataDeploymentBroker
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        object_meta_data_sla_dr_model = {} # ObjectMetaDataSlaDr
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        object_meta_data_template_environment_variables_model = {} # ObjectMetaDataTemplateEnvironmentVariables
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        object_meta_data_template_source_model = {} # ObjectMetaDataTemplateSource
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        urls_model = {} # URLS
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        callbacks_model = {} # Callbacks
        callbacks_model['broker_utl'] = 'testString'
        callbacks_model['broker_proxy_url'] = 'testString'
        callbacks_model['dashboard_url'] = 'testString'
        callbacks_model['dashboard_data_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_url'] = 'testString'
        callbacks_model['dashboard_detail_tab_ext_url'] = 'testString'
        callbacks_model['service_monitor_api'] = 'testString'
        callbacks_model['service_monitor_app'] = 'testString'
        callbacks_model['service_staging_url'] = 'testString'
        callbacks_model['service_production_url'] = 'testString'

        object_meta_data_alias_model = {} # ObjectMetaDataAlias
        object_meta_data_alias_model['type'] = 'testString'
        object_meta_data_alias_model['plan_id'] = 'testString'

        object_meta_data_deployment_model = {} # ObjectMetaDataDeployment
        object_meta_data_deployment_model['location'] = 'testString'
        object_meta_data_deployment_model['location_url'] = 'testString'
        object_meta_data_deployment_model['target_crn'] = 'testString'
        object_meta_data_deployment_model['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model['supports_rc_migration'] = True

        object_meta_data_plan_model = {} # ObjectMetaDataPlan
        object_meta_data_plan_model['bindable'] = True
        object_meta_data_plan_model['reservable'] = True
        object_meta_data_plan_model['allow_internal_users'] = True
        object_meta_data_plan_model['async_provisioning_supported'] = True
        object_meta_data_plan_model['async_unprovisioning_supported'] = True
        object_meta_data_plan_model['test_check_interval'] = 38
        object_meta_data_plan_model['single_scope_instance'] = 'testString'
        object_meta_data_plan_model['service_check_enabled'] = True
        object_meta_data_plan_model['cf_guid'] = 'testString'

        object_meta_data_service_model = {} # ObjectMetaDataService
        object_meta_data_service_model['type'] = 'testString'
        object_meta_data_service_model['iam_compatible'] = True
        object_meta_data_service_model['unique_api_key'] = True
        object_meta_data_service_model['provisionable'] = True
        object_meta_data_service_model['async_provisioning_supported'] = True
        object_meta_data_service_model['async_unprovisioning_supported'] = True
        object_meta_data_service_model['cf_guid'] = 'testString'
        object_meta_data_service_model['bindable'] = True
        object_meta_data_service_model['requires'] = ['testString']
        object_meta_data_service_model['plan_updateable'] = True
        object_meta_data_service_model['state'] = 'testString'
        object_meta_data_service_model['service_check_enabled'] = True
        object_meta_data_service_model['test_check_interval'] = 38
        object_meta_data_service_model['service_key_supported'] = True

        object_meta_data_sla_model = {} # ObjectMetaDataSla
        object_meta_data_sla_model['terms'] = 'testString'
        object_meta_data_sla_model['tenancy'] = 'testString'
        object_meta_data_sla_model['provisioning'] = 'testString'
        object_meta_data_sla_model['responsiveness'] = 'testString'
        object_meta_data_sla_model['dr'] = object_meta_data_sla_dr_model

        object_meta_data_template_model = {} # ObjectMetaDataTemplate
        object_meta_data_template_model['services'] = ['testString']
        object_meta_data_template_model['default_memory'] = 38
        object_meta_data_template_model['start_cmd'] = 'testString'
        object_meta_data_template_model['source'] = object_meta_data_template_source_model
        object_meta_data_template_model['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model['cf_runtime_id'] = 'testString'
        object_meta_data_template_model['template_id'] = 'testString'
        object_meta_data_template_model['executable_file'] = 'testString'
        object_meta_data_template_model['buildpack'] = 'testString'
        object_meta_data_template_model['environment_variables'] = object_meta_data_template_environment_variables_model

        pricing_model = {} # Pricing
        pricing_model['type'] = 'testString'
        pricing_model['origin'] = 'testString'
        pricing_model['starting_price'] = starting_price_model
        pricing_model['metrics'] = [metrics_model]

        ui_meta_data_model = {} # UIMetaData
        ui_meta_data_model['strings'] = i18_n_model
        ui_meta_data_model['urls'] = urls_model
        ui_meta_data_model['embeddable_dashboard'] = 'testString'
        ui_meta_data_model['embeddable_dashboard_full_width'] = True
        ui_meta_data_model['navigation_order'] = ['testString']
        ui_meta_data_model['not_creatable'] = True
        ui_meta_data_model['reservable'] = True
        ui_meta_data_model['primary_offering_id'] = 'testString'
        ui_meta_data_model['accessible_during_provision'] = True
        ui_meta_data_model['side_by_side_index'] = 38
        ui_meta_data_model['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ObjectMetaData model
        object_meta_data_model_json = {}
        object_meta_data_model_json['rc_compatible'] = True
        object_meta_data_model_json['ui'] = ui_meta_data_model
        object_meta_data_model_json['pricing'] = pricing_model
        object_meta_data_model_json['compliance'] = ['testString']
        object_meta_data_model_json['service'] = object_meta_data_service_model
        object_meta_data_model_json['plan'] = object_meta_data_plan_model
        object_meta_data_model_json['template'] = object_meta_data_template_model
        object_meta_data_model_json['deployment'] = object_meta_data_deployment_model
        object_meta_data_model_json['alias'] = object_meta_data_alias_model
        object_meta_data_model_json['sla'] = object_meta_data_sla_model
        object_meta_data_model_json['callbacks'] = callbacks_model
        object_meta_data_model_json['version'] = 'testString'
        object_meta_data_model_json['original_name'] = 'testString'
        object_meta_data_model_json['other'] = { 'foo': 'bar' }

        # Construct a model instance of ObjectMetaData by calling from_dict on the json representation
        object_meta_data_model = ObjectMetaData.from_dict(object_meta_data_model_json)
        assert object_meta_data_model != False

        # Construct a model instance of ObjectMetaData by calling from_dict on the json representation
        object_meta_data_model_dict = ObjectMetaData.from_dict(object_meta_data_model_json).__dict__
        object_meta_data_model2 = ObjectMetaData(**object_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_model == object_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_model_json2 = object_meta_data_model.to_dict()
        assert object_meta_data_model_json2 == object_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataAlias
#-----------------------------------------------------------------------------
class TestObjectMetaDataAlias():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataAlias
    #--------------------------------------------------------
    def test_object_meta_data_alias_serialization(self):

        # Construct a json representation of a ObjectMetaDataAlias model
        object_meta_data_alias_model_json = {}
        object_meta_data_alias_model_json['type'] = 'testString'
        object_meta_data_alias_model_json['plan_id'] = 'testString'

        # Construct a model instance of ObjectMetaDataAlias by calling from_dict on the json representation
        object_meta_data_alias_model = ObjectMetaDataAlias.from_dict(object_meta_data_alias_model_json)
        assert object_meta_data_alias_model != False

        # Construct a model instance of ObjectMetaDataAlias by calling from_dict on the json representation
        object_meta_data_alias_model_dict = ObjectMetaDataAlias.from_dict(object_meta_data_alias_model_json).__dict__
        object_meta_data_alias_model2 = ObjectMetaDataAlias(**object_meta_data_alias_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_alias_model == object_meta_data_alias_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_alias_model_json2 = object_meta_data_alias_model.to_dict()
        assert object_meta_data_alias_model_json2 == object_meta_data_alias_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataDeployment
#-----------------------------------------------------------------------------
class TestObjectMetaDataDeployment():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataDeployment
    #--------------------------------------------------------
    def test_object_meta_data_deployment_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        object_meta_data_deployment_broker_password_model = {} # ObjectMetaDataDeploymentBrokerPassword
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        object_meta_data_deployment_broker_model = {} # ObjectMetaDataDeploymentBroker
        object_meta_data_deployment_broker_model['name'] = 'testString'
        object_meta_data_deployment_broker_model['guid'] = 'testString'
        object_meta_data_deployment_broker_model['password'] = object_meta_data_deployment_broker_password_model

        # Construct a json representation of a ObjectMetaDataDeployment model
        object_meta_data_deployment_model_json = {}
        object_meta_data_deployment_model_json['location'] = 'testString'
        object_meta_data_deployment_model_json['location_url'] = 'testString'
        object_meta_data_deployment_model_json['target_crn'] = 'testString'
        object_meta_data_deployment_model_json['broker'] = object_meta_data_deployment_broker_model
        object_meta_data_deployment_model_json['supports_rc_migration'] = True

        # Construct a model instance of ObjectMetaDataDeployment by calling from_dict on the json representation
        object_meta_data_deployment_model = ObjectMetaDataDeployment.from_dict(object_meta_data_deployment_model_json)
        assert object_meta_data_deployment_model != False

        # Construct a model instance of ObjectMetaDataDeployment by calling from_dict on the json representation
        object_meta_data_deployment_model_dict = ObjectMetaDataDeployment.from_dict(object_meta_data_deployment_model_json).__dict__
        object_meta_data_deployment_model2 = ObjectMetaDataDeployment(**object_meta_data_deployment_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_deployment_model == object_meta_data_deployment_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_deployment_model_json2 = object_meta_data_deployment_model.to_dict()
        assert object_meta_data_deployment_model_json2 == object_meta_data_deployment_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataDeploymentBroker
#-----------------------------------------------------------------------------
class TestObjectMetaDataDeploymentBroker():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataDeploymentBroker
    #--------------------------------------------------------
    def test_object_meta_data_deployment_broker_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        object_meta_data_deployment_broker_password_model = {} # ObjectMetaDataDeploymentBrokerPassword
        object_meta_data_deployment_broker_password_model['text'] = 'testString'
        object_meta_data_deployment_broker_password_model['key'] = 'testString'
        object_meta_data_deployment_broker_password_model['iv'] = 'testString'

        # Construct a json representation of a ObjectMetaDataDeploymentBroker model
        object_meta_data_deployment_broker_model_json = {}
        object_meta_data_deployment_broker_model_json['name'] = 'testString'
        object_meta_data_deployment_broker_model_json['guid'] = 'testString'
        object_meta_data_deployment_broker_model_json['password'] = object_meta_data_deployment_broker_password_model

        # Construct a model instance of ObjectMetaDataDeploymentBroker by calling from_dict on the json representation
        object_meta_data_deployment_broker_model = ObjectMetaDataDeploymentBroker.from_dict(object_meta_data_deployment_broker_model_json)
        assert object_meta_data_deployment_broker_model != False

        # Construct a model instance of ObjectMetaDataDeploymentBroker by calling from_dict on the json representation
        object_meta_data_deployment_broker_model_dict = ObjectMetaDataDeploymentBroker.from_dict(object_meta_data_deployment_broker_model_json).__dict__
        object_meta_data_deployment_broker_model2 = ObjectMetaDataDeploymentBroker(**object_meta_data_deployment_broker_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_deployment_broker_model == object_meta_data_deployment_broker_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_deployment_broker_model_json2 = object_meta_data_deployment_broker_model.to_dict()
        assert object_meta_data_deployment_broker_model_json2 == object_meta_data_deployment_broker_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataDeploymentBrokerPassword
#-----------------------------------------------------------------------------
class TestObjectMetaDataDeploymentBrokerPassword():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataDeploymentBrokerPassword
    #--------------------------------------------------------
    def test_object_meta_data_deployment_broker_password_serialization(self):

        # Construct a json representation of a ObjectMetaDataDeploymentBrokerPassword model
        object_meta_data_deployment_broker_password_model_json = {}
        object_meta_data_deployment_broker_password_model_json['text'] = 'testString'
        object_meta_data_deployment_broker_password_model_json['key'] = 'testString'
        object_meta_data_deployment_broker_password_model_json['iv'] = 'testString'

        # Construct a model instance of ObjectMetaDataDeploymentBrokerPassword by calling from_dict on the json representation
        object_meta_data_deployment_broker_password_model = ObjectMetaDataDeploymentBrokerPassword.from_dict(object_meta_data_deployment_broker_password_model_json)
        assert object_meta_data_deployment_broker_password_model != False

        # Construct a model instance of ObjectMetaDataDeploymentBrokerPassword by calling from_dict on the json representation
        object_meta_data_deployment_broker_password_model_dict = ObjectMetaDataDeploymentBrokerPassword.from_dict(object_meta_data_deployment_broker_password_model_json).__dict__
        object_meta_data_deployment_broker_password_model2 = ObjectMetaDataDeploymentBrokerPassword(**object_meta_data_deployment_broker_password_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_deployment_broker_password_model == object_meta_data_deployment_broker_password_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_deployment_broker_password_model_json2 = object_meta_data_deployment_broker_password_model.to_dict()
        assert object_meta_data_deployment_broker_password_model_json2 == object_meta_data_deployment_broker_password_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataPlan
#-----------------------------------------------------------------------------
class TestObjectMetaDataPlan():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataPlan
    #--------------------------------------------------------
    def test_object_meta_data_plan_serialization(self):

        # Construct a json representation of a ObjectMetaDataPlan model
        object_meta_data_plan_model_json = {}
        object_meta_data_plan_model_json['bindable'] = True
        object_meta_data_plan_model_json['reservable'] = True
        object_meta_data_plan_model_json['allow_internal_users'] = True
        object_meta_data_plan_model_json['async_provisioning_supported'] = True
        object_meta_data_plan_model_json['async_unprovisioning_supported'] = True
        object_meta_data_plan_model_json['test_check_interval'] = 38
        object_meta_data_plan_model_json['single_scope_instance'] = 'testString'
        object_meta_data_plan_model_json['service_check_enabled'] = True
        object_meta_data_plan_model_json['cf_guid'] = 'testString'

        # Construct a model instance of ObjectMetaDataPlan by calling from_dict on the json representation
        object_meta_data_plan_model = ObjectMetaDataPlan.from_dict(object_meta_data_plan_model_json)
        assert object_meta_data_plan_model != False

        # Construct a model instance of ObjectMetaDataPlan by calling from_dict on the json representation
        object_meta_data_plan_model_dict = ObjectMetaDataPlan.from_dict(object_meta_data_plan_model_json).__dict__
        object_meta_data_plan_model2 = ObjectMetaDataPlan(**object_meta_data_plan_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_plan_model == object_meta_data_plan_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_plan_model_json2 = object_meta_data_plan_model.to_dict()
        assert object_meta_data_plan_model_json2 == object_meta_data_plan_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataService
#-----------------------------------------------------------------------------
class TestObjectMetaDataService():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataService
    #--------------------------------------------------------
    def test_object_meta_data_service_serialization(self):

        # Construct a json representation of a ObjectMetaDataService model
        object_meta_data_service_model_json = {}
        object_meta_data_service_model_json['type'] = 'testString'
        object_meta_data_service_model_json['iam_compatible'] = True
        object_meta_data_service_model_json['unique_api_key'] = True
        object_meta_data_service_model_json['provisionable'] = True
        object_meta_data_service_model_json['async_provisioning_supported'] = True
        object_meta_data_service_model_json['async_unprovisioning_supported'] = True
        object_meta_data_service_model_json['cf_guid'] = 'testString'
        object_meta_data_service_model_json['bindable'] = True
        object_meta_data_service_model_json['requires'] = ['testString']
        object_meta_data_service_model_json['plan_updateable'] = True
        object_meta_data_service_model_json['state'] = 'testString'
        object_meta_data_service_model_json['service_check_enabled'] = True
        object_meta_data_service_model_json['test_check_interval'] = 38
        object_meta_data_service_model_json['service_key_supported'] = True

        # Construct a model instance of ObjectMetaDataService by calling from_dict on the json representation
        object_meta_data_service_model = ObjectMetaDataService.from_dict(object_meta_data_service_model_json)
        assert object_meta_data_service_model != False

        # Construct a model instance of ObjectMetaDataService by calling from_dict on the json representation
        object_meta_data_service_model_dict = ObjectMetaDataService.from_dict(object_meta_data_service_model_json).__dict__
        object_meta_data_service_model2 = ObjectMetaDataService(**object_meta_data_service_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_service_model == object_meta_data_service_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_service_model_json2 = object_meta_data_service_model.to_dict()
        assert object_meta_data_service_model_json2 == object_meta_data_service_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataSla
#-----------------------------------------------------------------------------
class TestObjectMetaDataSla():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataSla
    #--------------------------------------------------------
    def test_object_meta_data_sla_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        object_meta_data_sla_dr_model = {} # ObjectMetaDataSlaDr
        object_meta_data_sla_dr_model['dr'] = True
        object_meta_data_sla_dr_model['description'] = 'testString'

        # Construct a json representation of a ObjectMetaDataSla model
        object_meta_data_sla_model_json = {}
        object_meta_data_sla_model_json['terms'] = 'testString'
        object_meta_data_sla_model_json['tenancy'] = 'testString'
        object_meta_data_sla_model_json['provisioning'] = 'testString'
        object_meta_data_sla_model_json['responsiveness'] = 'testString'
        object_meta_data_sla_model_json['dr'] = object_meta_data_sla_dr_model

        # Construct a model instance of ObjectMetaDataSla by calling from_dict on the json representation
        object_meta_data_sla_model = ObjectMetaDataSla.from_dict(object_meta_data_sla_model_json)
        assert object_meta_data_sla_model != False

        # Construct a model instance of ObjectMetaDataSla by calling from_dict on the json representation
        object_meta_data_sla_model_dict = ObjectMetaDataSla.from_dict(object_meta_data_sla_model_json).__dict__
        object_meta_data_sla_model2 = ObjectMetaDataSla(**object_meta_data_sla_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_sla_model == object_meta_data_sla_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_sla_model_json2 = object_meta_data_sla_model.to_dict()
        assert object_meta_data_sla_model_json2 == object_meta_data_sla_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataSlaDr
#-----------------------------------------------------------------------------
class TestObjectMetaDataSlaDr():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataSlaDr
    #--------------------------------------------------------
    def test_object_meta_data_sla_dr_serialization(self):

        # Construct a json representation of a ObjectMetaDataSlaDr model
        object_meta_data_sla_dr_model_json = {}
        object_meta_data_sla_dr_model_json['dr'] = True
        object_meta_data_sla_dr_model_json['description'] = 'testString'

        # Construct a model instance of ObjectMetaDataSlaDr by calling from_dict on the json representation
        object_meta_data_sla_dr_model = ObjectMetaDataSlaDr.from_dict(object_meta_data_sla_dr_model_json)
        assert object_meta_data_sla_dr_model != False

        # Construct a model instance of ObjectMetaDataSlaDr by calling from_dict on the json representation
        object_meta_data_sla_dr_model_dict = ObjectMetaDataSlaDr.from_dict(object_meta_data_sla_dr_model_json).__dict__
        object_meta_data_sla_dr_model2 = ObjectMetaDataSlaDr(**object_meta_data_sla_dr_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_sla_dr_model == object_meta_data_sla_dr_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_sla_dr_model_json2 = object_meta_data_sla_dr_model.to_dict()
        assert object_meta_data_sla_dr_model_json2 == object_meta_data_sla_dr_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataTemplate
#-----------------------------------------------------------------------------
class TestObjectMetaDataTemplate():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataTemplate
    #--------------------------------------------------------
    def test_object_meta_data_template_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        object_meta_data_template_environment_variables_model = {} # ObjectMetaDataTemplateEnvironmentVariables
        object_meta_data_template_environment_variables_model['_key_'] = 'testString'

        object_meta_data_template_source_model = {} # ObjectMetaDataTemplateSource
        object_meta_data_template_source_model['path'] = 'testString'
        object_meta_data_template_source_model['type'] = 'testString'
        object_meta_data_template_source_model['url'] = 'testString'

        # Construct a json representation of a ObjectMetaDataTemplate model
        object_meta_data_template_model_json = {}
        object_meta_data_template_model_json['services'] = ['testString']
        object_meta_data_template_model_json['default_memory'] = 38
        object_meta_data_template_model_json['start_cmd'] = 'testString'
        object_meta_data_template_model_json['source'] = object_meta_data_template_source_model
        object_meta_data_template_model_json['runtime_catalog_id'] = 'testString'
        object_meta_data_template_model_json['cf_runtime_id'] = 'testString'
        object_meta_data_template_model_json['template_id'] = 'testString'
        object_meta_data_template_model_json['executable_file'] = 'testString'
        object_meta_data_template_model_json['buildpack'] = 'testString'
        object_meta_data_template_model_json['environment_variables'] = object_meta_data_template_environment_variables_model

        # Construct a model instance of ObjectMetaDataTemplate by calling from_dict on the json representation
        object_meta_data_template_model = ObjectMetaDataTemplate.from_dict(object_meta_data_template_model_json)
        assert object_meta_data_template_model != False

        # Construct a model instance of ObjectMetaDataTemplate by calling from_dict on the json representation
        object_meta_data_template_model_dict = ObjectMetaDataTemplate.from_dict(object_meta_data_template_model_json).__dict__
        object_meta_data_template_model2 = ObjectMetaDataTemplate(**object_meta_data_template_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_template_model == object_meta_data_template_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_template_model_json2 = object_meta_data_template_model.to_dict()
        assert object_meta_data_template_model_json2 == object_meta_data_template_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataTemplateEnvironmentVariables
#-----------------------------------------------------------------------------
class TestObjectMetaDataTemplateEnvironmentVariables():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataTemplateEnvironmentVariables
    #--------------------------------------------------------
    def test_object_meta_data_template_environment_variables_serialization(self):

        # Construct a json representation of a ObjectMetaDataTemplateEnvironmentVariables model
        object_meta_data_template_environment_variables_model_json = {}
        object_meta_data_template_environment_variables_model_json['_key_'] = 'testString'

        # Construct a model instance of ObjectMetaDataTemplateEnvironmentVariables by calling from_dict on the json representation
        object_meta_data_template_environment_variables_model = ObjectMetaDataTemplateEnvironmentVariables.from_dict(object_meta_data_template_environment_variables_model_json)
        assert object_meta_data_template_environment_variables_model != False

        # Construct a model instance of ObjectMetaDataTemplateEnvironmentVariables by calling from_dict on the json representation
        object_meta_data_template_environment_variables_model_dict = ObjectMetaDataTemplateEnvironmentVariables.from_dict(object_meta_data_template_environment_variables_model_json).__dict__
        object_meta_data_template_environment_variables_model2 = ObjectMetaDataTemplateEnvironmentVariables(**object_meta_data_template_environment_variables_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_template_environment_variables_model == object_meta_data_template_environment_variables_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_template_environment_variables_model_json2 = object_meta_data_template_environment_variables_model.to_dict()
        assert object_meta_data_template_environment_variables_model_json2 == object_meta_data_template_environment_variables_model_json

#-----------------------------------------------------------------------------
# Test Class for ObjectMetaDataTemplateSource
#-----------------------------------------------------------------------------
class TestObjectMetaDataTemplateSource():

    #--------------------------------------------------------
    # Test serialization/deserialization for ObjectMetaDataTemplateSource
    #--------------------------------------------------------
    def test_object_meta_data_template_source_serialization(self):

        # Construct a json representation of a ObjectMetaDataTemplateSource model
        object_meta_data_template_source_model_json = {}
        object_meta_data_template_source_model_json['path'] = 'testString'
        object_meta_data_template_source_model_json['type'] = 'testString'
        object_meta_data_template_source_model_json['url'] = 'testString'

        # Construct a model instance of ObjectMetaDataTemplateSource by calling from_dict on the json representation
        object_meta_data_template_source_model = ObjectMetaDataTemplateSource.from_dict(object_meta_data_template_source_model_json)
        assert object_meta_data_template_source_model != False

        # Construct a model instance of ObjectMetaDataTemplateSource by calling from_dict on the json representation
        object_meta_data_template_source_model_dict = ObjectMetaDataTemplateSource.from_dict(object_meta_data_template_source_model_json).__dict__
        object_meta_data_template_source_model2 = ObjectMetaDataTemplateSource(**object_meta_data_template_source_model_dict)

        # Verify the model instances are equivalent
        assert object_meta_data_template_source_model == object_meta_data_template_source_model2

        # Convert model instance back to dict and verify no loss of data
        object_meta_data_template_source_model_json2 = object_meta_data_template_source_model.to_dict()
        assert object_meta_data_template_source_model_json2 == object_meta_data_template_source_model_json

#-----------------------------------------------------------------------------
# Test Class for Overview
#-----------------------------------------------------------------------------
class TestOverview():

    #--------------------------------------------------------
    # Test serialization/deserialization for Overview
    #--------------------------------------------------------
    def test_overview_serialization(self):

        # Construct a json representation of a Overview model
        overview_model_json = {}
        overview_model_json['display_name'] = 'testString'
        overview_model_json['long_description'] = 'testString'
        overview_model_json['description'] = 'testString'

        # Construct a model instance of Overview by calling from_dict on the json representation
        overview_model = Overview.from_dict(overview_model_json)
        assert overview_model != False

        # Construct a model instance of Overview by calling from_dict on the json representation
        overview_model_dict = Overview.from_dict(overview_model_json).__dict__
        overview_model2 = Overview(**overview_model_dict)

        # Verify the model instances are equivalent
        assert overview_model == overview_model2

        # Convert model instance back to dict and verify no loss of data
        overview_model_json2 = overview_model.to_dict()
        assert overview_model_json2 == overview_model_json

#-----------------------------------------------------------------------------
# Test Class for OverviewUI
#-----------------------------------------------------------------------------
class TestOverviewUI():

    #--------------------------------------------------------
    # Test serialization/deserialization for OverviewUI
    #--------------------------------------------------------
    def test_overview_ui_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        overview_model = {} # Overview
        overview_model['display_name'] = 'testString'
        overview_model['long_description'] = 'testString'
        overview_model['description'] = 'testString'

        # Construct a json representation of a OverviewUI model
        overview_ui_model_json = {}
        overview_ui_model_json['foo'] = overview_model

        # Construct a model instance of OverviewUI by calling from_dict on the json representation
        overview_ui_model = OverviewUI.from_dict(overview_ui_model_json)
        assert overview_ui_model != False

        # Construct a model instance of OverviewUI by calling from_dict on the json representation
        overview_ui_model_dict = OverviewUI.from_dict(overview_ui_model_json).__dict__
        overview_ui_model2 = OverviewUI(**overview_ui_model_dict)

        # Verify the model instances are equivalent
        assert overview_ui_model == overview_ui_model2

        # Convert model instance back to dict and verify no loss of data
        overview_ui_model_json2 = overview_ui_model.to_dict()
        assert overview_ui_model_json2 == overview_ui_model_json

#-----------------------------------------------------------------------------
# Test Class for Price
#-----------------------------------------------------------------------------
class TestPrice():

    #--------------------------------------------------------
    # Test serialization/deserialization for Price
    #--------------------------------------------------------
    def test_price_serialization(self):

        # Construct a json representation of a Price model
        price_model_json = {}
        price_model_json['quantity_tier'] = 38
        price_model_json['Price'] = 36.0

        # Construct a model instance of Price by calling from_dict on the json representation
        price_model = Price.from_dict(price_model_json)
        assert price_model != False

        # Construct a model instance of Price by calling from_dict on the json representation
        price_model_dict = Price.from_dict(price_model_json).__dict__
        price_model2 = Price(**price_model_dict)

        # Verify the model instances are equivalent
        assert price_model == price_model2

        # Convert model instance back to dict and verify no loss of data
        price_model_json2 = price_model.to_dict()
        assert price_model_json2 == price_model_json

#-----------------------------------------------------------------------------
# Test Class for Pricing
#-----------------------------------------------------------------------------
class TestPricing():

    #--------------------------------------------------------
    # Test serialization/deserialization for Pricing
    #--------------------------------------------------------
    def test_pricing_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        amount_model = {} # Amount
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        metrics_model = {} # Metrics
        metrics_model['metric_id'] = 'testString'
        metrics_model['tier_model'] = 'testString'
        metrics_model['charge_unit_name'] = 'testString'
        metrics_model['charge_unit_quantity'] = 'testString'
        metrics_model['resource_display_name'] = 'testString'
        metrics_model['charge_unit_display_name'] = 'testString'
        metrics_model['usage_cap_qty'] = 38
        metrics_model['amounts'] = [amount_model]

        starting_price_model = {} # StartingPrice
        starting_price_model['plan_id'] = 'testString'
        starting_price_model['deployment_id'] = 'testString'
        starting_price_model['amount'] = [amount_model]

        # Construct a json representation of a Pricing model
        pricing_model_json = {}
        pricing_model_json['type'] = 'testString'
        pricing_model_json['origin'] = 'testString'
        pricing_model_json['starting_price'] = starting_price_model
        pricing_model_json['metrics'] = [metrics_model]

        # Construct a model instance of Pricing by calling from_dict on the json representation
        pricing_model = Pricing.from_dict(pricing_model_json)
        assert pricing_model != False

        # Construct a model instance of Pricing by calling from_dict on the json representation
        pricing_model_dict = Pricing.from_dict(pricing_model_json).__dict__
        pricing_model2 = Pricing(**pricing_model_dict)

        # Verify the model instances are equivalent
        assert pricing_model == pricing_model2

        # Convert model instance back to dict and verify no loss of data
        pricing_model_json2 = pricing_model.to_dict()
        assert pricing_model_json2 == pricing_model_json

#-----------------------------------------------------------------------------
# Test Class for Provider
#-----------------------------------------------------------------------------
class TestProvider():

    #--------------------------------------------------------
    # Test serialization/deserialization for Provider
    #--------------------------------------------------------
    def test_provider_serialization(self):

        # Construct a json representation of a Provider model
        provider_model_json = {}
        provider_model_json['email'] = 'testString'
        provider_model_json['name'] = 'testString'
        provider_model_json['contact'] = 'testString'
        provider_model_json['support_email'] = 'testString'
        provider_model_json['phone'] = 'testString'

        # Construct a model instance of Provider by calling from_dict on the json representation
        provider_model = Provider.from_dict(provider_model_json)
        assert provider_model != False

        # Construct a model instance of Provider by calling from_dict on the json representation
        provider_model_dict = Provider.from_dict(provider_model_json).__dict__
        provider_model2 = Provider(**provider_model_dict)

        # Verify the model instances are equivalent
        assert provider_model == provider_model2

        # Convert model instance back to dict and verify no loss of data
        provider_model_json2 = provider_model.to_dict()
        assert provider_model_json2 == provider_model_json

#-----------------------------------------------------------------------------
# Test Class for Scope
#-----------------------------------------------------------------------------
class TestScope():

    #--------------------------------------------------------
    # Test serialization/deserialization for Scope
    #--------------------------------------------------------
    def test_scope_serialization(self):

        # Construct a json representation of a Scope model
        scope_model_json = {}
        scope_model_json['type'] = 'testString'
        scope_model_json['value'] = 'testString'

        # Construct a model instance of Scope by calling from_dict on the json representation
        scope_model = Scope.from_dict(scope_model_json)
        assert scope_model != False

        # Construct a model instance of Scope by calling from_dict on the json representation
        scope_model_dict = Scope.from_dict(scope_model_json).__dict__
        scope_model2 = Scope(**scope_model_dict)

        # Verify the model instances are equivalent
        assert scope_model == scope_model2

        # Convert model instance back to dict and verify no loss of data
        scope_model_json2 = scope_model.to_dict()
        assert scope_model_json2 == scope_model_json

#-----------------------------------------------------------------------------
# Test Class for SearchResult
#-----------------------------------------------------------------------------
class TestSearchResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for SearchResult
    #--------------------------------------------------------
    def test_search_result_serialization(self):

        # Construct a json representation of a SearchResult model
        search_result_model_json = {}
        search_result_model_json['page'] = 'testString'
        search_result_model_json['results_per_page'] = 'testString'
        search_result_model_json['total_results'] = 'testString'
        search_result_model_json['resources'] = [{ 'foo': 'bar' }]

        # Construct a model instance of SearchResult by calling from_dict on the json representation
        search_result_model = SearchResult.from_dict(search_result_model_json)
        assert search_result_model != False

        # Construct a model instance of SearchResult by calling from_dict on the json representation
        search_result_model_dict = SearchResult.from_dict(search_result_model_json).__dict__
        search_result_model2 = SearchResult(**search_result_model_dict)

        # Verify the model instances are equivalent
        assert search_result_model == search_result_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_model_json2 = search_result_model.to_dict()
        assert search_result_model_json2 == search_result_model_json

#-----------------------------------------------------------------------------
# Test Class for StartingPrice
#-----------------------------------------------------------------------------
class TestStartingPrice():

    #--------------------------------------------------------
    # Test serialization/deserialization for StartingPrice
    #--------------------------------------------------------
    def test_starting_price_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        price_model = {} # Price
        price_model['quantity_tier'] = 38
        price_model['Price'] = 36.0

        amount_model = {} # Amount
        amount_model['counrty'] = 'testString'
        amount_model['currency'] = 'testString'
        amount_model['prices'] = [price_model]

        # Construct a json representation of a StartingPrice model
        starting_price_model_json = {}
        starting_price_model_json['plan_id'] = 'testString'
        starting_price_model_json['deployment_id'] = 'testString'
        starting_price_model_json['amount'] = [amount_model]

        # Construct a model instance of StartingPrice by calling from_dict on the json representation
        starting_price_model = StartingPrice.from_dict(starting_price_model_json)
        assert starting_price_model != False

        # Construct a model instance of StartingPrice by calling from_dict on the json representation
        starting_price_model_dict = StartingPrice.from_dict(starting_price_model_json).__dict__
        starting_price_model2 = StartingPrice(**starting_price_model_dict)

        # Verify the model instances are equivalent
        assert starting_price_model == starting_price_model2

        # Convert model instance back to dict and verify no loss of data
        starting_price_model_json2 = starting_price_model.to_dict()
        assert starting_price_model_json2 == starting_price_model_json

#-----------------------------------------------------------------------------
# Test Class for Strings
#-----------------------------------------------------------------------------
class TestStrings():

    #--------------------------------------------------------
    # Test serialization/deserialization for Strings
    #--------------------------------------------------------
    def test_strings_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        # Construct a json representation of a Strings model
        strings_model_json = {}
        strings_model_json['bullets'] = [bullets_model]
        strings_model_json['media'] = [ui_meta_media_model]
        strings_model_json['not_creatable_msg'] = 'testString'
        strings_model_json['not_creatable__robot_msg'] = 'testString'
        strings_model_json['deprecation_warning'] = 'testString'
        strings_model_json['popup_warning_message'] = 'testString'
        strings_model_json['instruction'] = 'testString'

        # Construct a model instance of Strings by calling from_dict on the json representation
        strings_model = Strings.from_dict(strings_model_json)
        assert strings_model != False

        # Construct a model instance of Strings by calling from_dict on the json representation
        strings_model_dict = Strings.from_dict(strings_model_json).__dict__
        strings_model2 = Strings(**strings_model_dict)

        # Verify the model instances are equivalent
        assert strings_model == strings_model2

        # Convert model instance back to dict and verify no loss of data
        strings_model_json2 = strings_model.to_dict()
        assert strings_model_json2 == strings_model_json

#-----------------------------------------------------------------------------
# Test Class for UIMetaData
#-----------------------------------------------------------------------------
class TestUIMetaData():

    #--------------------------------------------------------
    # Test serialization/deserialization for UIMetaData
    #--------------------------------------------------------
    def test_ui_meta_data_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        ui_meta_media_model = {} # UIMetaMedia
        ui_meta_media_model['caption'] = 'testString'
        ui_meta_media_model['thumbnail_url'] = 'testString'
        ui_meta_media_model['type'] = 'testString'
        ui_meta_media_model['URL'] = 'testString'
        ui_meta_media_model['source'] = bullets_model

        strings_model = {} # Strings
        strings_model['bullets'] = [bullets_model]
        strings_model['media'] = [ui_meta_media_model]
        strings_model['not_creatable_msg'] = 'testString'
        strings_model['not_creatable__robot_msg'] = 'testString'
        strings_model['deprecation_warning'] = 'testString'
        strings_model['popup_warning_message'] = 'testString'
        strings_model['instruction'] = 'testString'

        i18_n_model = {} # I18N
        i18_n_model['foo'] = strings_model

        urls_model = {} # URLS
        urls_model['doc_url'] = 'testString'
        urls_model['instructions_url'] = 'testString'
        urls_model['api_url'] = 'testString'
        urls_model['create_url'] = 'testString'
        urls_model['sdk_download_url'] = 'testString'
        urls_model['terms_url'] = 'testString'
        urls_model['custom_create_page_url'] = 'testString'
        urls_model['catalog_details_url'] = 'testString'
        urls_model['deprecation_doc_url'] = 'testString'

        # Construct a json representation of a UIMetaData model
        ui_meta_data_model_json = {}
        ui_meta_data_model_json['strings'] = i18_n_model
        ui_meta_data_model_json['urls'] = urls_model
        ui_meta_data_model_json['embeddable_dashboard'] = 'testString'
        ui_meta_data_model_json['embeddable_dashboard_full_width'] = True
        ui_meta_data_model_json['navigation_order'] = ['testString']
        ui_meta_data_model_json['not_creatable'] = True
        ui_meta_data_model_json['reservable'] = True
        ui_meta_data_model_json['primary_offering_id'] = 'testString'
        ui_meta_data_model_json['accessible_during_provision'] = True
        ui_meta_data_model_json['side_by_side_index'] = 38
        ui_meta_data_model_json['end_of_service_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of UIMetaData by calling from_dict on the json representation
        ui_meta_data_model = UIMetaData.from_dict(ui_meta_data_model_json)
        assert ui_meta_data_model != False

        # Construct a model instance of UIMetaData by calling from_dict on the json representation
        ui_meta_data_model_dict = UIMetaData.from_dict(ui_meta_data_model_json).__dict__
        ui_meta_data_model2 = UIMetaData(**ui_meta_data_model_dict)

        # Verify the model instances are equivalent
        assert ui_meta_data_model == ui_meta_data_model2

        # Convert model instance back to dict and verify no loss of data
        ui_meta_data_model_json2 = ui_meta_data_model.to_dict()
        assert ui_meta_data_model_json2 == ui_meta_data_model_json

#-----------------------------------------------------------------------------
# Test Class for UIMetaMedia
#-----------------------------------------------------------------------------
class TestUIMetaMedia():

    #--------------------------------------------------------
    # Test serialization/deserialization for UIMetaMedia
    #--------------------------------------------------------
    def test_ui_meta_media_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        bullets_model = {} # Bullets
        bullets_model['title'] = 'testString'
        bullets_model['description'] = 'testString'
        bullets_model['icon'] = 'testString'
        bullets_model['quantity'] = 'testString'

        # Construct a json representation of a UIMetaMedia model
        ui_meta_media_model_json = {}
        ui_meta_media_model_json['caption'] = 'testString'
        ui_meta_media_model_json['thumbnail_url'] = 'testString'
        ui_meta_media_model_json['type'] = 'testString'
        ui_meta_media_model_json['URL'] = 'testString'
        ui_meta_media_model_json['source'] = bullets_model

        # Construct a model instance of UIMetaMedia by calling from_dict on the json representation
        ui_meta_media_model = UIMetaMedia.from_dict(ui_meta_media_model_json)
        assert ui_meta_media_model != False

        # Construct a model instance of UIMetaMedia by calling from_dict on the json representation
        ui_meta_media_model_dict = UIMetaMedia.from_dict(ui_meta_media_model_json).__dict__
        ui_meta_media_model2 = UIMetaMedia(**ui_meta_media_model_dict)

        # Verify the model instances are equivalent
        assert ui_meta_media_model == ui_meta_media_model2

        # Convert model instance back to dict and verify no loss of data
        ui_meta_media_model_json2 = ui_meta_media_model.to_dict()
        assert ui_meta_media_model_json2 == ui_meta_media_model_json

#-----------------------------------------------------------------------------
# Test Class for URLS
#-----------------------------------------------------------------------------
class TestURLS():

    #--------------------------------------------------------
    # Test serialization/deserialization for URLS
    #--------------------------------------------------------
    def test_urls_serialization(self):

        # Construct a json representation of a URLS model
        urls_model_json = {}
        urls_model_json['doc_url'] = 'testString'
        urls_model_json['instructions_url'] = 'testString'
        urls_model_json['api_url'] = 'testString'
        urls_model_json['create_url'] = 'testString'
        urls_model_json['sdk_download_url'] = 'testString'
        urls_model_json['terms_url'] = 'testString'
        urls_model_json['custom_create_page_url'] = 'testString'
        urls_model_json['catalog_details_url'] = 'testString'
        urls_model_json['deprecation_doc_url'] = 'testString'

        # Construct a model instance of URLS by calling from_dict on the json representation
        urls_model = URLS.from_dict(urls_model_json)
        assert urls_model != False

        # Construct a model instance of URLS by calling from_dict on the json representation
        urls_model_dict = URLS.from_dict(urls_model_json).__dict__
        urls_model2 = URLS(**urls_model_dict)

        # Verify the model instances are equivalent
        assert urls_model == urls_model2

        # Convert model instance back to dict and verify no loss of data
        urls_model_json2 = urls_model.to_dict()
        assert urls_model_json2 == urls_model_json

#-----------------------------------------------------------------------------
# Test Class for Visibility
#-----------------------------------------------------------------------------
class TestVisibility():

    #--------------------------------------------------------
    # Test serialization/deserialization for Visibility
    #--------------------------------------------------------
    def test_visibility_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        visibility_detail_accounts_model = {} # VisibilityDetailAccounts
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        scope_model = {} # Scope
        scope_model['type'] = 'testString'
        scope_model['value'] = 'testString'

        visibility_detail_model = {} # VisibilityDetail
        visibility_detail_model['accounts'] = visibility_detail_accounts_model

        # Construct a json representation of a Visibility model
        visibility_model_json = {}
        visibility_model_json['restrictions'] = 'testString'
        visibility_model_json['owner'] = scope_model
        visibility_model_json['include'] = visibility_detail_model
        visibility_model_json['exclude'] = visibility_detail_model
        visibility_model_json['approved'] = True

        # Construct a model instance of Visibility by calling from_dict on the json representation
        visibility_model = Visibility.from_dict(visibility_model_json)
        assert visibility_model != False

        # Construct a model instance of Visibility by calling from_dict on the json representation
        visibility_model_dict = Visibility.from_dict(visibility_model_json).__dict__
        visibility_model2 = Visibility(**visibility_model_dict)

        # Verify the model instances are equivalent
        assert visibility_model == visibility_model2

        # Convert model instance back to dict and verify no loss of data
        visibility_model_json2 = visibility_model.to_dict()
        assert visibility_model_json2 == visibility_model_json

#-----------------------------------------------------------------------------
# Test Class for VisibilityDetail
#-----------------------------------------------------------------------------
class TestVisibilityDetail():

    #--------------------------------------------------------
    # Test serialization/deserialization for VisibilityDetail
    #--------------------------------------------------------
    def test_visibility_detail_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        visibility_detail_accounts_model = {} # VisibilityDetailAccounts
        visibility_detail_accounts_model['_accountid_'] = 'testString'

        # Construct a json representation of a VisibilityDetail model
        visibility_detail_model_json = {}
        visibility_detail_model_json['accounts'] = visibility_detail_accounts_model

        # Construct a model instance of VisibilityDetail by calling from_dict on the json representation
        visibility_detail_model = VisibilityDetail.from_dict(visibility_detail_model_json)
        assert visibility_detail_model != False

        # Construct a model instance of VisibilityDetail by calling from_dict on the json representation
        visibility_detail_model_dict = VisibilityDetail.from_dict(visibility_detail_model_json).__dict__
        visibility_detail_model2 = VisibilityDetail(**visibility_detail_model_dict)

        # Verify the model instances are equivalent
        assert visibility_detail_model == visibility_detail_model2

        # Convert model instance back to dict and verify no loss of data
        visibility_detail_model_json2 = visibility_detail_model.to_dict()
        assert visibility_detail_model_json2 == visibility_detail_model_json

#-----------------------------------------------------------------------------
# Test Class for VisibilityDetailAccounts
#-----------------------------------------------------------------------------
class TestVisibilityDetailAccounts():

    #--------------------------------------------------------
    # Test serialization/deserialization for VisibilityDetailAccounts
    #--------------------------------------------------------
    def test_visibility_detail_accounts_serialization(self):

        # Construct a json representation of a VisibilityDetailAccounts model
        visibility_detail_accounts_model_json = {}
        visibility_detail_accounts_model_json['_accountid_'] = 'testString'

        # Construct a model instance of VisibilityDetailAccounts by calling from_dict on the json representation
        visibility_detail_accounts_model = VisibilityDetailAccounts.from_dict(visibility_detail_accounts_model_json)
        assert visibility_detail_accounts_model != False

        # Construct a model instance of VisibilityDetailAccounts by calling from_dict on the json representation
        visibility_detail_accounts_model_dict = VisibilityDetailAccounts.from_dict(visibility_detail_accounts_model_json).__dict__
        visibility_detail_accounts_model2 = VisibilityDetailAccounts(**visibility_detail_accounts_model_dict)

        # Verify the model instances are equivalent
        assert visibility_detail_accounts_model == visibility_detail_accounts_model2

        # Convert model instance back to dict and verify no loss of data
        visibility_detail_accounts_model_json2 = visibility_detail_accounts_model.to_dict()
        assert visibility_detail_accounts_model_json2 == visibility_detail_accounts_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
