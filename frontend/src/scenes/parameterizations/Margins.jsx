import React from "react";
import ReactDOM from "react-dom";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import MainCheckBoxInput from "../../components/inputs/MainCheckBoxInput";
import MainColorInput from "../../components/inputs/MainColorInput";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import LoadingGif from "../../components/visual/LoadingGif";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class Margins extends React.Component {
   constructor(props) {
      super(props)
      this.state = {
         alertType: '',
         alertMessage: '',
         showAlert: false,

         isLoading: true,
         isLoadingTab: true,
         isLoadingMarginsTable: true,
         isLoadingMarginsStructureTable: true,

         isANewMargins: false,
         menuId: '30',

         margins: {},
         marginsList: [],
         marginsColumns: {},
         marginsTotalSize: '',

         marginsStructureList: [],
         marginsStructureColumns: {},
         marginsStructureTotalSize: '',

         marginsStructure: {
            idproduto: null,
            familia: null,
            grupo: null,
            ggrupo: null,
            sgrupo: null,
            marca: null,
            categoria: null,
            fabricante: null,
            origem: null,
            linha: null,
            perminimo: 0,
            permaximo: 0,
         },

         search: '',
         status: 'A',
         marginsCode: '',
         statusOptions: [
            { 'value': 'A', 'label': 'Ativo' },
            { 'value': 'B', 'label': 'Bloqueado' },
            { 'value': 'X', 'label': 'Cancelado' },
         ],
         tabs: [
            { id: 'data', title: 'Margens' },
            { id: 'marginproduct', title: 'Margens x Produto' },
         ],
      }
   }

   closeEditTab = () => {
      var element = document.getElementById('edit-tab')
      element.parentNode.removeChild(element)
      this.onMarginsTableChange(0)
   }

   componentDidMount() {
      addLastAccess(this.state.menuId)
      this.onMarginsTableChange(0)
      optionsRequest(this, ['bigGroup', 'brand', 'category', 'family', 'group', 'manufacturer', 'origin', 'product', 'productLine', 'subGroup'])
   }

   createEditTab = (params, isRegister = false) => {
      if (isRegister) {
         this.setState({
            selectedRow: params,
            isLoadingTab: true,
            activeTab: 'data',
            margins: {
               visivel: false,
               valor: false,
               cor1: '#AFAFAF',
               cor2: '#AFAFAF',
               cor3: '#AFAFAF',
            },
            tabs: [{ id: 'data', title: 'Margens' }],
         }, () => createEditTab('Criação de Margens de Contribuição', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
      } else {
         this.setState({
            isANewPortalMessage: false,
            selectedRow: params,
            isLoadingTab: true,
            tabs: [
               { id: 'data', title: 'Margens' },
               { id: 'marginproduct', title: 'Margens x Produto' },
            ],
         }, () => createEditTab('Configuração das Margens de Contribuição', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
      }
   }

   deleteMarginStructure = (id) => {
      let config = {
         method: 'delete',
         endpoint: 'product/margins/structure/single'
      }
      let form = {
         id: id
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState({
               alertMessage: r.data.message,
               alertType: 'success',
               showAlert: true,
            }, () => this.onMarginsStructureTableChange(0))
         } else {
            this.setState({
               alertMessage: r.data.message,
               alertType: 'error',
               showAlert: true
            })
         }
      })
   }

   handleChangeTab = (event) => {
      if (this.state.isLoadingTab && !this.state.isANewMargins) {
         ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchMarginsInfo())
         return
      }
      if (!this.state.margins && !this.state.isANewMargins) {
         return
      }
      var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

      changeActiveTabStyle(this.state.tabs, page, this.props.colors)

      var context = ''
      if (page === 'data') {
         context =
            <Box sx={{ flexGrow: 1 }}>
               <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                  <Grid item md={2}><MainTextField {...this.props} type='number' id='idmargem' value={this.state.margins.idmargem} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>
                  <Grid item md={7}><MainTextField required {...this.props} id='desmargem' value={this.state.margins.desmargem} label='Descrição' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '98%' }} /></Grid>
                  <Grid item md={3}><MainSelectInput required {...this.props} id='situacao' value={this.state.margins.situacao || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} /></Grid>

                  <Grid item md={6}>
                     <Box display='flex' flexDirection='row' marginBottom='10px'>
                        <Grid item md={4}><MainCheckBoxInput {...this.props} id='visivel' value={this.state.margins.visivel} label='Visível' handleChange={this.handleChangeTextTab} /></Grid>
                        <Grid item md={6}><MainCheckBoxInput {...this.props} id='valor' value={this.state.margins.valor} label='Valor' handleChange={this.handleChangeTextTab} /></Grid>
                     </Box>

                     <Box
                        width='95%'
                        height='80%'
                        border='2px solid'
                        borderRadius='5px'
                        padding='0 10px 10px 10px'
                        borderColor={this.props.colors.grey[700]}
                     >
                        <Grid container columnSpacing={1} rowSpacing={2} alignItems='center' sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, alignItems: 'center' }}>
                           <Grid item md={12}><MainLabel {...this.props} variant="tabSubSubTitle" label="Configuração de Cores" /></Grid>

                           <Grid item md={8}><span style={{ fontSize: '16px' }} >Desejável</span></Grid>
                           <Grid item md={4}><MainColorInput {...this.props} id='cor1' value={this.state.margins.cor1} handleChange={this.handleChangeTextTab} /></Grid>

                           <Grid item md={8}><span style={{ fontSize: '16px' }} >Acima do Desejável</span></Grid>
                           <Grid item md={4}><MainColorInput {...this.props} id='cor2' value={this.state.margins.cor2} handleChange={this.handleChangeTextTab} /></Grid>

                           <Grid item md={8}><span style={{ fontSize: '16px' }} >Abaixo do Desejável</span></Grid>
                           <Grid item md={4}><MainColorInput {...this.props} id='cor3' value={this.state.margins.cor3} handleChange={this.handleChangeTextTab} /></Grid>

                        </Grid>
                     </Box>

                  </Grid>

                  <Grid item md={6}>
                     <Box
                        width='98%'
                        height='100%'
                        border='2px solid'
                        borderRadius='5px'
                        padding='0 10px 10px 10px'
                        borderColor={this.props.colors.grey[700]}
                     >
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, alignItems: 'center' }}>
                           <Grid item md={12}><MainLabel {...this.props} variant="tabSubSubTitle" label="Produto" /></Grid>
                           <Grid item md={6} ><MainTextField required {...this.props} type='percent' id='perminproduto' value={this.state.margins.perminproduto} label='Mínimo (%)' handleChange={this.handleChangeTextTab} /></Grid>
                           <Grid item md={6} ><MainTextField required {...this.props} type='percent' id='perdesproduto' value={this.state.margins.perdesproduto} label='Desejável (%)' handleChange={this.handleChangeTextTab} /></Grid>

                           <Grid item md={12}><MainLabel {...this.props} variant="tabSubSubTitle" label="Pedido" /></Grid>
                           <Grid item md={6} ><MainTextField required {...this.props} type='percent' id='perminpedido' value={this.state.margins.perminpedido} label='Mínimo (%)' handleChange={this.handleChangeTextTab} /></Grid>
                           <Grid item md={6} ><MainTextField required {...this.props} type='percent' id='perdespedido' value={this.state.margins.perdespedido} label='Desejável (%)' handleChange={this.handleChangeTextTab} /></Grid>
                        </Grid>
                     </Box>
                  </Grid>

                  <MainTabButton sx={{ width: { xs: '96.5%', sm: '96.5%', md: '15%'}, margin: '15px 0 0 10px' }} {...this.props} onButtonClick={this.saveOrUpdateMargins} title="Salvar" />

               </Grid>
            </Box>
      } else if (page === 'marginproduct') {
         if (this.state.isLoadingMarginsStructureTable) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onMarginsStructureTableChange(0))
            return
         }
         context =
            <Box sx={{ flexGrow: 1 }}>
               <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0 0 0' }}>
                  <Grid item md={12}><MainSelectInput required {...this.props} id='idproduto' value={this.state.marginsStructure.idproduto || ''} optionsList={this.state.productOptions} label='Produto' handleChange={this.handleChangeTextTabSelects} width={{ xs: '94%', sm: '94%', md: '98%' }} /></Grid>
                  <Grid item md={4}><MainSelectInput {...this.props} id='familia' value={this.state.marginsStructure.familia || ''} optionsList={this.state.familyOptions} label='Família' handleChange={this.handleChangeTextTabSelects} /></Grid>
                  <Grid item md={4}><MainSelectInput {...this.props} id='ggrupo' value={this.state.marginsStructure.ggrupo || ''} optionsList={this.state.bigGroupOptions} label='Grande Grupo' handleChange={this.handleChangeTextTabSelects} /></Grid>
                  <Grid item md={4}><MainSelectInput {...this.props} id='grupo' value={this.state.marginsStructure.grupo || ''} optionsList={this.state.groupOptions} label='Grupo' handleChange={this.handleChangeTextTabSelects} /></Grid>
                  <Grid item md={4}><MainSelectInput {...this.props} id='sgrupo' value={this.state.marginsStructure.sgrupo || ''} optionsList={this.state.subGroupOptions} label='Sub Grupo' handleChange={this.handleChangeTextTabSelects} /></Grid>
                  <Grid item md={4}><MainSelectInput {...this.props} id='marca' value={this.state.marginsStructure.marca || ''} optionsList={this.state.brandOptions} label='Marca' handleChange={this.handleChangeTextTabSelects} disabled={true} /></Grid>
                  <Grid item md={4}><MainSelectInput {...this.props} id='categoria' value={this.state.marginsStructure.categoria || ''} optionsList={this.state.categoryOptions} label='Categoria' handleChange={this.handleChangeTextTabSelects} /></Grid>
                  <Grid item md={8}><MainSelectInput {...this.props} id='fabricante' value={this.state.marginsStructure.fabricante || ''} optionsList={this.state.manufacturerOptions} label='Fabricante' handleChange={this.handleChangeTextTabSelects} disabled={true} width={{ sm: '94%', md: '97%' }} /></Grid>
                  <Grid item md={4}><MainSelectInput {...this.props} id='origem' value={this.state.marginsStructure.origem || ''} optionsList={this.state.originOptions} label='Origem' handleChange={this.handleChangeTextTabSelects} /></Grid>
                  <Grid item md={4}><MainSelectInput {...this.props} id='linha' value={this.state.marginsStructure.linha || ''} optionsList={this.state.productLineOptions} label='Linha' handleChange={this.handleChangeTextTabSelects} /></Grid>

                  <Grid item md={2}><MainTextField {...this.props} type='percent' id='perminimo' value={this.state.marginsStructure.perminimo || ''} label='Mínimo (%)' handleChange={this.handleChangeTextTabSelects} /></Grid>
                  <Grid item md={2}><MainTextField {...this.props} type='percent' id='permaximo' value={this.state.marginsStructure.permaximo || ''} label='Máximo (%)' handleChange={this.handleChangeTextTabSelects} width={{ xs: '94%', sm: '94%', md: '88%' }} /></Grid>

                  <Grid item md={4}>
                     <MainTabButton width='94%' {...this.props} onButtonClick={this.includeMarginStructure} title="Inserir" />
                  </Grid>
                  
               </Grid>

               <Box
                  margin='0 10px 0 10px'
               >
                  <EditableTable
                     {...this.props}
                     allowEdit
                     noEditButton
                     height='55vh'
                     id='marginsStructureTable'
                     data={this.state.marginsStructureList}
                     columns={this.state.marginsStructureColumns}
                     rowId='idmarestrutura'
                     totalSize={this.state.marginsStructureTotalSize}
                     onPageChange={this.onMarginsStructureTableChange}
                     onEditRow={this.onMarginsStructureTableEdit}
                     onRowDoubleClick={() => { }}
                     isLoading={this.state.isLoadingMarginsStructureTable}
                     extraColumnsConfig={
                        {
                           'idproduto_id': {
                              'type': 'select',
                              'options': this.state.productOptions
                           },
                           'familia_id': {
                              'type': 'select',
                              'options': this.state.familyOptions
                           },
                           'ggrupo_id': {
                              'type': 'select',
                              'options': this.state.bigGroupOptions
                           },
                           'grupo_id': {
                              'type': 'select',
                              'options': this.state.groupOptions
                           },
                           'sgrupo_id': {
                              'type': 'select',
                              'options': this.state.subGroupOptions
                           },
                           'marca_id': {
                              'type': 'select',
                              'options': this.state.brandOptions
                           },
                           'categoria_id': {
                              'type': 'select',
                              'options': this.state.categoryOptions
                           },
                           'fabricante_id': {
                              'type': 'select',
                              'options': this.state.manufacturerOptions
                           },
                           'origem_id': {
                              'type': 'select',
                              'options': this.state.originOptions
                           },
                           'linha_id': {
                              'type': 'select',
                              'options': this.state.productLineOptions
                           },
                           'perminimo': {
                              'type': 'percent'
                           },
                           'permaximo': {
                              'type': 'percent'
                           },
                        }
                     }
                  />
               </Box>
            </Box>
      }
      ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
   }

   handleChangeText = (event) => {
      this.setState({ [event.target.id]: event.target.value })
   }

   handleChangeTextTab = (event) => {
      handleChangeText(this.state.margins, event.target.id, event.target.value, () => this.handleChangeTab())
   }

   handleChangeTextTabSelects = (event) => {
      handleChangeText(this.state.marginsStructure, event.target.id, event.target.value, () => this.handleChangeTab())
   }

   includeMarginStructure = () => {
      if (!this.state.marginsStructure.familia &&
         !this.state.marginsStructure.ggrupo &&
         !this.state.marginsStructure.grupo &&
         !this.state.marginsStructure.sgrupo &&
         !this.state.marginsStructure.marca &&
         !this.state.marginsStructure.categoria &&
         !this.state.marginsStructure.fabricante &&
         !this.state.marginsStructure.origem &&
         !this.state.marginsStructure.linha
      ) {
         this.setState({
            alertMessage: 'Necessário selecionar uma das opções para o produto',
            alertType: 'error',
            showAlert: true
         })
         return
      }
      if (!this.state.marginsStructure.idproduto) {
         this.setState({
            alertMessage: 'Necessário selecionar um produto',
            alertType: 'error',
            showAlert: true
         })
         return
      }
      let config = {
         method: 'post',
         endpoint: 'product/margins/structure/single'
      }
      let form = {
         id: this.state.selectedRow.idmargem,
         marginsStructure: this.state.marginsStructure,
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState({
               alertMessage: r.data.message,
               alertType: 'success',
               showAlert: true,

            }, () => this.onMarginsStructureTableChange(0))
         } else {
            this.setState({
               alertMessage: r.data.message,
               alertType: 'error',
               showAlert: true
            })
         }
      })

   }

   onCloseEditTab = () => {
      this.setState({
         activeTab: 'data',
         isLoadingTab: true,
         isLoadingMarginsStructureTable: true,
         isANewMargins: false,
         margins: {},
         marginsStructure: {},
      })
   }

   onMarginsStructureTableChange = (page) => {
      let config = {
         method: 'get',
         endpoint: 'product/margins/structure/single'
      }
      let form = {
         id: this.state.selectedRow.idmargem,
         page: page,
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState({
               marginsStructureList: r.data.margin_structure,
               marginsStructureColumns: r.data.columns,
               marginsStructureTotalSize: r.data.total_size,

               isLoadingMarginsStructureTable: false,
               activeTab: 'marginproduct',
            }, () => this.handleChangeTab())
         }
      })
   }

   onMarginsStructureTableEdit = (row, method, extraParam) => {
      if (method === 'delete') {
         this.setState({
            marginsStructureList: row // Atualiza a lista, sem a linha que foi excluída
         }, () => this.deleteMarginStructure(extraParam)) // extraParam = Id da linha que foi excluída
      }
   }

   onMarginsTableChange = (page) => {
      let config = {
         method: 'get',
         endpoint: 'product/margins/search'
      }
      let form = {
         page: page,
         search: this.state.search,
         marginsCode: this.state.marginsCode,
         status: this.state.status
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState({
               marginsList: r.data.margins,
               marginsColumns: r.data.columns,
               marginsTotalSize: r.data.total_size,

               isLoading: false,
               isLoadingMarginsTable: false,
            })
         }
      })
   }

   saveOrUpdateMargins = () => {
      let config = {
         method: 'post',
         endpoint: 'product/margins/single'
      }
      let form = {
         id: this.state.margins.idmargem,
         margins: this.state.margins,
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            var newState = {
               alertMessage: r.data.message,
               alertType: 'success',
               showAlert: true,
            }

            if (this.state.isANewMargins) {
               newState['isANewMargins'] = false
               this.closeEditTab()
            }

            this.setState(prevState => ({
               ...prevState, ...newState
            }))
         } else {
            this.setState({
               alertMessage: r.data.message,
               alertType: 'error',
               showAlert: true
            })
         }
      })
   }

   saveProductStructure = () => {
      // let config = {
      //    method: 'post',
      //    endpoint: 'salesregion/single'
      // }
      // let form = {
      //    id: this.state.selectedRow.idregiao,
      //    infos: {
      //       cidade: this.state.selectCity,
      //       uf: this.state.selectUf,
      //    },
      //    type: 'addUfCity'
      // }
   }

   searchMarginsInfo = () => {
      if (this.state.isANewMargins) {
         this.setState({ isLoadingTab: false })
         return
      }
      let config = {
         method: 'get',
         endpoint: 'product/margins/single'
      }
      let form = {
         id: this.state.selectedRow.idmargem
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            var margins = r.data.margins
            margins.visivel = margins.visivel === 'S'
            margins.valor = margins.valor === 'S'

            this.setState({
               margins: margins,
               isLoadingTab: false,
            }, () => this.handleChangeTab())
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
               <Header {...this.props} title='Margens' menuId={this.state.menuId} showFav />
               <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                  <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                  <Box
                     mr='40px'
                     display='grid'
                     gap='15px'
                     sx={{
                        mr: '40px',
                        display: 'grid',
                        gap: '15px',
                        gridTemplateColumns: {
                           md: '100%',
                           lg: '10% 40% 17% 10% 10% 10%',
                        },
                     }}
                  >
                     <MainTextField {...this.props} type='number' id='marginsCode' value={this.state.marginsCode} label='Código' handleChange={this.handleChangeText} width='100%' />
                     <MainTextField {...this.props} id='search' value={this.state.search} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                     <MainSelectInput {...this.props} id='status' value={this.state.status || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />

                     <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onMarginsTableChange(0)}>Buscar</Button>
                     <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ marginsCode: '', search: '', status: 'A' })}>Limpar</Button>
                     <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewMargins: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                  </Box>

                  <EditableTable
                     {...this.props}
                     id='marginsTable'
                     allowEdit
                     noDeleteButton
                     data={this.state.marginsList}
                     columns={this.state.marginsColumns}
                     rowId='idmargem'
                     totalSize={this.state.marginsTotalSize}
                     onPageChange={this.onMarginsTableChange}
                     onEditRow={() => { }}
                     onRowDoubleClick={(params) => this.createEditTab(params, false)}
                     isLoading={this.state.isLoadingMarginsTable}
                     extraColumnsConfig={
                        {
                           'idmargem': {
                              'type': 'number',
                           },
                           'situacao': {
                              'type': 'select',
                              'options': this.state.statusOptions
                           },
                           'cor1': {
                              'type': 'color'
                           },
                           'cor2': {
                              'type': 'color'
                           },
                           'cor3': {
                              'type': 'color'
                           },
                           'perminproduto': {
                              'type': 'percent'
                           },
                           'perdesproduto': {
                              'type': 'percent'
                           },
                           'perminpedido': {
                              'type': 'percent'
                           },
                           'perdespedido': {
                              'type': 'percent'
                           },
                        }
                     }
                  />
               </Box>
            </Box>
         </>
      )
   }
}

export default Margins;