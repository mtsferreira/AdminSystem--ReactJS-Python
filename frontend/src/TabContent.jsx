import React from 'react';
import { TabsContext } from './TabsContext'; // Importe seu contexto de abas

import AccessGroup from './scenes/hidden/AccessGroup';
import ComercialDiscount from "./scenes/parameterizations/ComercialDiscount";
import Company from "./scenes/companiesAndLocalSale/Company";
import CommissionDiscount from './scenes/commercialPolicies/CommissionDiscount';
import CommissionPolicies from './scenes/commercialPolicies/CommissionPolicies';
import Customers from "./scenes/customersAndReps/Customers";
import CustomerTypeDiscount from './scenes/commercialPolicies/CustomerTypeDiscount';
import DashboardGraphics from "./scenes/managementIndicators/DashboardGraphics";
import LocalSale from "./scenes/companiesAndLocalSale/LocalSale";
import Margins from "./scenes/parameterizations/Margins";
import Offers from './scenes/commercialPolicies/Offers';
import OrderBook from "./scenes/budgetAndOrderManagement/OrderBook";
import OrderType from "./scenes/parameterizations/OrderType";
import PaymentConditions from "./scenes/parameterizations/PaymentConditions";
import PaymentTerm from "./scenes/parameterizations/PaymentTerm";
import PriceRules from "./scenes/parameterizations/PriceRules";
import Prices from "./scenes/prices/Prices";
import PortalMessage from "./scenes/parameterizations/PortalMessage";
import PriceStructure from './scenes/commercialPolicies/PriceStructure';
import ProductLines from "./scenes/parameterizations/ProductLines";
import ProductRegister from "./scenes/products/ProductRegister";
import Represented from "./scenes/customersAndReps/Represented";
import SalesRegion from "./scenes/parameterizations/SalesRegion";
import ShippingCif from './scenes/commercialPolicies/ShippingCif';
import Shortcuts from "./scenes/hidden/Shortcuts";
import Users from "./scenes/hidden/User";
import VolumeDiscount from "./scenes/commercialPolicies/VolumeDiscount";
import WorkFlow from "./scenes/parameterizations/WorkFlow";
import WorkFlowBudget from './scenes/budgetAndOrderManagement/WorkFlowBudget';


class TabContent extends React.Component {
  static contextType = TabsContext;

  render() {
    const { tabs, activeTab } = this.context
    const activeTabInfo = tabs.find(tab => tab.key === activeTab)

    const components = {
        '2': { component: <DashboardGraphics {...this.props} /> },
        '4': { component: <Customers {...this.props} /> },
        '5': { component: <Represented {...this.props} /> },
        '7': { component: <ProductRegister {...this.props} /> },
        '9': { component: <Prices {...this.props} /> },
        '11': { component: <WorkFlowBudget {...this.props} />, },
        '12': { component: <OrderBook {...this.props} /> },
        '14': { component: <Company {...this.props} /> },
        '15': { component: <LocalSale {...this.props} /> },
        '17': { component: <Offers {...this.props} /> },
        '18': { component: <CommissionPolicies {...this.props} /> },
        '19': { component: <CommissionDiscount {...this.props} /> },
        '20': { component: <PriceStructure {...this.props} /> },
        '21': { component: 'Preço x Prazo', },
        '22': { component: <VolumeDiscount {...this.props} /> },
        '23': { component: <CustomerTypeDiscount {...this.props} /> },
        '24': { component: <ShippingCif {...this.props} /> },
        '38': { component: <OrderType {...this.props} /> },
        '26': { component: <PaymentConditions {...this.props} /> },
        '27': { component: <PaymentTerm {...this.props} /> },
        '28': { component: <ComercialDiscount {...this.props} /> },
        '29': { component: <ProductLines {...this.props} /> },
        '30': { component: <Margins {...this.props} /> },
        '31': { component: <PriceRules {...this.props} /> },
        '32': { component: <PortalMessage {...this.props} /> },
        '33': { component: <SalesRegion {...this.props} /> },
        '34': { component: <WorkFlow {...this.props} /> },
        '36': { component: <AccessGroup {...this.props} /> },
        '37': { component: <Users {...this.props} /> },
    }

    return (
        <>
            {/* <div className="tab-content">
                {activeTabInfo ? components[activeTabInfo.key].component : 'Selecione uma aba ou abra uma nova.'}
            </div> */}
            <div className="tab-contents">
                {tabs.map(tab => (
                    <div 
                        key={tab.key} 
                        style={{ display: tab.key === activeTab ? 'block' : 'none' }}
                    >
                        {components[tab.key].component}
                    </div>
                ))}
            </div>
        </>
    )
  }
}

export default TabContent