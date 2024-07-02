import React from "react";

import dayjs from "dayjs";
import 'dayjs/locale/pt-br';

// Component Pages
import Login from "./scenes/login/Login";
import TabBar from "./TabBar";
import TabContent from "./TabContent";

// Component Globals
import Navbar from "./scenes/global/Navbar";
import Sidebar from "./scenes/global/Sidebar";

import { ColorModeContext, useMode } from "./typograhpy";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { defaultRequest } from "./utils/request/request";
import { Routes, Route } from "react-router-dom";
import { TabsProvider } from './TabsContext';
import { tokens } from "./typograhpy";

// CSS
import './css/main.css'


function withHooks(WrappedComponent) {
  return function(props) {
    const [theme, colorMode] = useMode()
    const colors = tokens(theme.palette.mode)
    
    return (
      <WrappedComponent colors={colors} colorMode={colorMode} theme={theme} {...props} />
    )
  }
}

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      isLoaded: true,
      loggedIn: false,
      isCollapsed: false,
      user: {},
      activeTab: '',
      tabs: [],
      activeTab: ''
    }
    dayjs.locale('pt-br')
  }

  componentDidMount() {

    const userToken = localStorage.getItem('userToken')

    if (!userToken) {
      this.setState({loggedIn: false})
    }
    else {
      defaultRequest({method:'get', endpoint: 'verify'}, {token: userToken}).then((r) => {
        if (r.status) {
          this.setState({loggedIn: true, user: r.data.user})
        } else {
          localStorage.removeItem('userToken')
        }
      })
    }
  }

  handleCollapse = () => {
    this.setState({
      isCollapsed: !this.state.isCollapsed,
      hoverSidebar: !this.state.isCollapsed ? true : false
    }, () => this.changeSidebarWidth())
  }

  handleMouseEnter = () => {
    if (this.state.hoverSidebar) {
      this.setState({
        isCollapsed: !this.state.isCollapsed
      })
    }
  }

  changeSidebarWidth = () => {
    var el = document.getElementsByClassName('content3')[0]
    if(this.state.isCollapsed) {
      el.classList.toggle('animate');
      el.classList.remove('max-sidebar')
      el.classList.add('min-sidebar')

    } else {
      el.classList.toggle('animate');
      el.classList.remove('min-sidebar')
      el.classList.add('max-sidebar')
    }
  }

  switchTab = (title) => {
    this.setState({activeTab: title})
  }

  render() {
    if(!this.state.loggedIn) {
      return(<Login />)
    }
    return (
      <TabsProvider>
      <ColorModeContext.Provider value={this.props.colorMode}>
      <ThemeProvider theme={this.props.theme}>
        <CssBaseline />
        <div className="app" id='app'>
          <main className="content">
            <Navbar {...this.props} user={this.state.user} handleCollapse={this.handleCollapse}  />
            <main className="content2">
              <Sidebar {...this.props} user={this.state.user} isCollapsed={this.state.isCollapsed} hoverSidebar={this.state.hoverSidebar} handleMouseEnter={this.handleMouseEnter} activeTab={this.state.activeTab} switchTab={this.switchTab} />
              <main className="content3 max-sidebar">
              <TabBar {...this.props} user={this.state.user} switchTab={this.switchTab}/>
              <TabContent {...this.props} user={this.state.user} />
                {/* <Routes>
                  <Route path='/comercialdiscount' element={<ComercialDiscount {...this.props} user={this.state.user} />} />
                  <Route path='/company' element={<Company {...this.props} user={this.state.user} />} />
                  <Route path='/customers' element={<Customers {...this.props} user={this.state.user} />} />
                  <Route path='/graphics' element={<DashboardGraphics {...this.props} user={this.state.user} />} />
                  <Route path='/localsale' element={<LocalSale {...this.props} user={this.state.user} />} />
                  <Route path='/margins' element={<Margins {...this.props} user={this.state.user} />} />
                  <Route path='/orderbook' element={<OrderBook {...this.props} user={this.state.user} />} />
                  <Route path='/ordertype' element={<OrderType {...this.props} user={this.state.user} />} />
                  <Route path='/payment' element={<PaymentConditions {...this.props} user={this.state.user} />} />
                  <Route path='/paymentterm' element={<PaymentTerm {...this.props} user={this.state.user} />} />
                  <Route path='/pricerules' element={<PriceRules {...this.props} user={this.state.user} />} />
                  <Route path='/prices' element={<Prices {...this.props} user={this.state.user} />} />
                  <Route path='/portalmessage' element={<PortalMessage {...this.props} user={this.state.user} />} />
                  <Route path='/productlines' element={<ProductLines {...this.props} user={this.state.user} />} />
                  <Route path='/productregister' element={<ProductRegister {...this.props} user={this.state.user} />} />
                  <Route path='/represented' element={<Represented {...this.props} user={this.state.user} />} />
                  <Route path='/salesregion' element={<SalesRegion {...this.props} user={this.state.user} />} />
                  <Route path='/usuarios' element={<Users />} />
                  <Route path='/workflow' element={<WorkFlow {...this.props} user={this.state.user} />} />
                  <Route path='' element={<Shortcuts {...this.props} user={this.state.user} />} />
                </Routes> */}
              </main>
            </main>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
    </TabsProvider>
    )
  }
}

export default withHooks(App)