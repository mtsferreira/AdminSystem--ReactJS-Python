CUSTOMER_SELLER_QUERY = '''
select 
	cv.IDClienteVendedor as idclientevendedor,
	c.coderp as coderp,
	u.Nome as nome,
    tu.Descricao as tipousuario,
	CASE WHEN ev.IDEquipe is not null THEN evv.DesEquipe ELSE u.nome END as equipe,
	cs.DesCascata as descontocomercial,
	v.DesVolume as descontovolume
from Cliente c
inner join ClienteVendedor cv on c.IDCliente = cv.IDCliente
inner join Usuario u on u.IDUsuario = cv.IDUsuario
inner join TipoUsuario tu on tu.IDTipoUsuario = u.TipoUsuario
inner join Cascata cs on cs.idcascata = cv.IDCascata
inner join Volume v on v.IDVolume = cv.IDVolume
left join EquipeVendedor ev on ev.IDUsuario = u.IDUsuario
left join EquipeVenda evv on evv.IDEquipe = ev.IDEquipe
where c.IDCliente=%s and u.TipoUsuario in (1,6,7);
'''