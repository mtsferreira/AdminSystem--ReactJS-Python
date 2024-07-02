import React from "react";
import ReactDOM from "react-dom";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import LoadingGif from "../../components/visual/LoadingGif";
import MainDateTimeInput from "../../components/inputs/MainDateTimeInput";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class PaymentTerm extends React.Component {
   constructor(props) {
      super(props)
      this.state = {
         alertType: '',
         alertMessage: '',
         showAlert: false,

         isLoading: true,
         isLoadingPaymentTable: true,
         isLoadingTermTable: true,
         isLoadingTab: true,
         menuId: '27',

         term: '',
         status: 'A',

         termDays: '',
         termIncrease: '',
         termDiscount: '',
         termMinValue: '',

         paymentList: [],
         paymentColumns: {},
         paymentTotalSize: '',

         termList: [],
         termColumns: {},
         termTotalSize: '',

         statusOptions: [
            { 'value': 'A', 'label': 'Ativo' },
            { 'value': 'B', 'label': 'Bloqueado' },
            { 'value': 'X', 'label': 'Cancelado' },
         ],

         activeTab: 'data',
         tabs: [
            { id: 'data', title: 'Dados' },
         ],
      }
   }

   componentDidMount() {
      addLastAccess(this.state.menuId)
      this.onPaymentTableChange(0)
   }

   createEditTab = (params, isRegister = false) => {
      this.setState({
         isANewOrderType: isRegister ? true : false,
         selectedRow: params,
         isLoadingTab: true,
      }, () => createEditTab('Variação de Preços por Prazo de Pagamento', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
   }

   deletePayment = (id) => {
      let config = {
         method: 'delete',
         endpoint: 'financial/term'
      }
      let form = {
         id: id,
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState(({
               alertMessage: r.data.message,
               alertType: 'success',
               showAlert: true,

               isLoadingPaymentTable: true
            }), () => this.onPaymentTableChange(0))
         } else {
            this.setState({
               alertMessage: r.data.message,
               alertType: 'error',
               showAlert: true
            })
         }
      })
   }

   deleteTerm = (id) => {
      let config = {
         method: 'delete',
         endpoint: 'financial/term/range'
      }
      let form = {
         paymentId: this.state.selectedRow.idprazofinanceiro,
         id: id,
      }
      defaultRequest(config, form).then((r) => {
         this.setState({
            alertMessage: r.data.message,
            alertType: r.status ? 'success' : 'error',
            showAlert: true,
         }, r.status ? () => this.onTermTableChange(0) : () => { })
      })
   }

   handleChangeTab = (event) => {
      if (this.state.isLoadingTab && !this.state.isANewOrderType) {
         ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchPaymentTerm())
         return
      }
      var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

      changeActiveTabStyle(this.state.tabs, page, this.props.colors)

      var context = ''
      if (page === 'data') {
         if (this.state.isLoadingTermTable) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onTermTableChange(0))
            return
         }
         context =
            <Box sx={{ flexGrow: 1 }}>
               <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                  <Grid item md={2}><MainTextField required {...this.props} id='idprazofinanceiro' value={this.state.paymentTerm.idprazofinanceiro || ''} label='Código' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                  <Grid item md={7}><MainTextField required {...this.props} id='descprazo' value={this.state.paymentTerm.descprazo || ''} label='Descrição da Variação' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                  <Grid item md={3}><MainSelectInput required {...this.props} id='situacao' value={this.state.paymentTerm.situacao || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                  <Grid item md={3}><MainDateTimeInput {...this.props} type='date' onlyDate id='datainicial' value={this.state.paymentTerm.datainicial || ''} label='Data Inicial' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                  <Grid item md={3}><MainDateTimeInput {...this.props} type='date' onlyDate id='datafinal' value={this.state.paymentTerm.datafinal || ''} label='Data Final' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                  <Grid item md={3}></Grid>

                  <Grid item md={3}>
                     <MainTabButton width='97%' {...this.props} onButtonClick={this.savePayment} title="Salvar" />
                  </Grid>

                  <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="" /></Grid>
                  <Grid item md={5}>
                     <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                        <Grid item md={6}><MainTextField required {...this.props} id='termDays' value={this.state.termDays || ''} label='Prazo em Dias' handleChange={this.handleChangeTextNewTerm} fullWidth /></Grid>
                        <Grid item md={6}><MainTextField required {...this.props} type='percent' id='termIncrease' value={this.state.termIncrease || ''} label='Aumento (%)' handleChange={this.handleChangeTextNewTerm} fullWidth /></Grid>
                        <Grid item md={6}><MainTextField required {...this.props} type='percent' id='termDiscount' value={this.state.termDiscount || ''} label='Desconto (%)' handleChange={this.handleChangeTextNewTerm} fullWidth /></Grid>
                        <Grid item md={6}><MainTextField required {...this.props} type='percent' id='termMinValue' value={this.state.termMinValue || ''} label='Valor Mínimo' handleChange={this.handleChangeTextNewTerm} fullWidth /></Grid>

                        <Grid item md={6}>
                           <MainTabButton width='97%' {...this.props} onButtonClick={this.saveTerm} title="Inserir" />
                        </Grid>

                     </Grid>
                  </Grid>
                  <Grid item md={7}>
                     <EditableTable
                        {...this.props}
                        allowEdit
                        noEditButton
                        customMargin='0'
                        height='40vh'
                        id='idprazofaixa'
                        data={this.state.termList}
                        columns={this.state.termColumns}
                        rowId={'idprazofaixa'}
                        totalSize={this.state.termTotalSize}
                        onPageChange={this.onTermTableChange}
                        onEditRow={this.onTermTableEdit}
                        onRowDoubleClick={() => { }}
                        isLoading={this.state.isLoadingTermTable}
                        extraColumnsConfig={
                           {
                              'situacao': {
                                 'type': 'select',
                                 'options': this.state.statusOptions
                              },
                              'perdesconto': {
                                 'type': 'percent',
                              },
                              'peracrescimo': {
                                 'type': 'percent',
                              },
                           }
                        }
                     />
                  </Grid>
               </Grid>
            </Box>
      }
      ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
   }

   handleChangeText = (event) => {
      this.setState({ [event.target.id]: event.target.value })
   }

   handleChangeTextTab = (event) => {
      handleChangeText(this.state.paymentTerm, event.target.id, event.target.value, () => this.handleChangeTab())
   }

   handleChangeTextNewTerm = (event) => {
      this.setState({ [event.target.id]: event.target.value }, () => this.handleChangeTab())
   }

   onCloseEditTab = () => {
      this.setState({
         isLoadingPaymentTable: true,
         isLoadingTab: true,
         isLoadingTermTable: true,
         paymentTerm: {},
      }, () => this.onPaymentTableChange(0))
   }

   onPaymentTableChange = (page) => {
      this.setState({ isLoadingPaymentTable: true })
      let config = {
         method: 'get',
         endpoint: 'financial/term'
      }
      let form = {
         page: page,
         term: this.state.term,
         status: this.state.status
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState({
               paymentList: r.data.financial,
               paymentColumns: r.data.columns,
               paymentTotalSize: r.data.total_size,
               isLoading: false,
               isLoadingPaymentTable: false
            })
         }
      })
   }

   onTermTableChange = (page) => {
      this.setState({ isLoadingTermTable: true })
      let config = {
         method: 'get',
         endpoint: 'financial/term/range'
      }
      let form = {
         page: page,
         id: this.state.selectedRow.idprazofinanceiro
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState({
               termList: r.data.financial,
               termColumns: r.data.columns,
               termTotalSize: r.data.total_size,
               isLoadingTermTable: false
            }, () => this.handleChangeTab())
         }
      })
   }

   onTermTableEdit = (row, method, extraParam) => {
      if (method === 'delete') {
         this.setState({
            termList: row
         }, () => this.deleteTerm(extraParam))
      }
   }

   savePayment = () => {
      let config = {
         method: 'post',
         endpoint: 'financial/term/single'
      }
      let form = {
         id: this.state.selectedRow.idprazofinanceiro,
         paymentTerm: this.state.paymentTerm
      }
      defaultRequest(config, form).then((r) => {
         this.setState({
            alertMessage: r.data.message,
            alertType: r.status ? 'success' : 'error',
            showAlert: true,
         })
      })
   }

   saveTerm = () => {
      let config = {
         method: 'post',
         endpoint: 'financial/term/range'
      }
      let form = {
         id: this.state.selectedRow.idprazofinanceiro,
         termRange: {
            prazodias: this.state.termDays,
            perdesconto: this.state.termDiscount,
            peracrescimo: this.state.termIncrease,
            vlminimo: this.state.termMinValue
         }
      }
      defaultRequest(config, form).then((r) => {
         this.setState({
            alertMessage: r.data.message,
            alertType: r.status ? 'success' : 'error',
            showAlert: true,
         }, r.status ? () => this.onTermTableChange(0) : () => { })
      })
   }

   searchPaymentTerm = () => {
      let config = {
         method: 'get',
         endpoint: 'financial/term/single'
      }
      let form = {
         id: this.state.selectedRow.idprazofinanceiro,
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState(({
               paymentTerm: r.data.term,
               isLoadingTab: false
            }), () => this.handleChangeTab())
         }
      })
   }


   render() {
      if (this.state.isLoading) {
         return (
            <></>
         )
      }
      return (
         <>
            {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({ showAlert: false, alertMessage: '' })} /> : <></>}
            <Box className='outline-box'>
               <Header {...this.props} title='Prazo de Pagamento' menuId={this.state.menuId} showFav />
               <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                  <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                  {/* SEARCHING FIELDS */}
                  <Box
                     sx={{
                        mr: '45px',
                        display: 'grid',
                        gap: '20px',
                        gridTemplateColumns: {
                           md: '100%',
                           lg: '60% 20% 20%',
                        },
                     }}
                  >
                     <MainTextField {...this.props} type='number' id='term' value={this.state.term || ''} label='Código' handleChange={this.handleChangeText} width='100%' />
                     <MainSelectInput {...this.props} id='status' value={this.state.status || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />
                     <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.onPaymentTableChange(0)}>Buscar</Button>
                  </Box>
                  <EditableTable
                     {...this.props}
                     allowEdit
                     noDeleteButton
                     id='idprazofinanceiro'
                     data={this.state.paymentList}
                     columns={this.state.paymentColumns}
                     rowId={'idprazofinanceiro'}
                     totalSize={this.state.paymentTotalSize}
                     onPageChange={this.onPaymentTableChange}
                     onRowDoubleClick={(params) => this.createEditTab(params)}
                     isLoading={this.state.isLoadingPaymentTable}
                     extraColumnsConfig={
                        {
                           'idprazofinanceiro': {
                              'type': 'number'
                           },
                           'situacao': {
                              'type': 'select',
                              'options': this.state.statusOptions
                           },
                           'datainicial': {
                              'type': 'date'
                           },
                           'datafinal': {
                              'type': 'date'
                           }
                        }
                     }
                  />
               </Box>
            </Box>
         </>
      )
   }
}

export default PaymentTerm;