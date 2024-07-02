export function getNestedProperty(obj, path) {
    return path.split('.').reduce((currentObject, key) => {
        return currentObject ? currentObject[key] : undefined;
    }, obj);
}

export function formatPhone(phoneNumber) {
    const cleanNumber = phoneNumber.replace(/\D/g, '')
  
    if (cleanNumber.length === 10) {
      return cleanNumber.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3')
    } else if (cleanNumber.length === 11) {
      return cleanNumber.replace(/(\d{2})(\d)(\d{4})(\d{4})/, '($1) $2 $3-$4')
    } else {
      return phoneNumber
    }
}

export function formatValueAsReal(value) {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL'
  }).format(value)
}