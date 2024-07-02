import React from "react";

import { TextField } from "@mui/material";

class MainTextField extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <TextField className="main-text-field"
                id={this.props.id ?? undefined}
                sx={{
                    height: '100%',
                    '& .MuiInputBase-root': {
                        height: '100%',
                        fontSize: '16px' // Tamanho da fonte da label
                    },
                    '& label.Mui-focused': {
                        color: this.props.colors.blueAccent[400],
                    },
                    '& label': {
                        color: this.props.colors.grey[400],
                    },
                    '& .MuiInput-underline:after': {
                        borderBottomColor: this.props.colors.blueAccent[400],
                    },
                    '& .MuiOutlinedInput-root': {
                        '& fieldset': {
                            borderColor: this.props.colors.grey[1100],
                        },
                        // '&:hover fieldset': {
                        //     borderColor: 'yellow',
                        // },
                        '&.Mui-focused fieldset': {
                            borderColor: this.props.colors.blueAccent[400],
                        },
                    },
                    '& .MuiInputBase-multiline': {
                        color: this.props.colors.grey[100],
                    },
                    input: {
                        textAlign: ['number', 'percent', 'currency'].includes(this.props.type) ? 'right' : 'left',
                        color: this.props.colors.grey[100]
                    },
                    '& .MuiInputBase-input.Mui-disabled': {
                        WebkitTextFillColor: this.props.colors.grey[100],
                        backgroundColor: this.props.colors.primary[400], // Background do campo quando desabilitado
                        borderRadius: '4px',
                        opacity: 0.7
                    },
                    label: {
                        fontSize: '16px',
                        "&.Mui-disabled": {
                            fontSize: '16px', // Tamanho da fonte da label quando desabilitado
                            color: this.props.colors.grey[400]
                        }
                    },
                    width: this.props.width ? this.props.width : this.props.fullWidth ? '97%' : '94%'
                }}
                variant={this.props.borderless ? 'standard' : 'outlined'}
                type={this.props.type === 'number' || this.props.type === 'percent' ? 'number' : 'text'}
                disabled={this.props.disabled ?? false}
                multiline={this.props.minRows ? true : false}

                rows={this.props.minRows ?? 1}
                value={this.props.value ?? undefined}
                label={
                    this.props.required
                        ? <>{this.props.label}<span style={{ color: this.props.colors.blueAccent['400'] }}> *</span></> ?? ''
                        : this.props.label ?? ''
                }
                size={this.props.size ?? 'small'}
                fullWidth={this.props.fullWidth ? true : false}
                InputProps={{
                    endAdornment: this.props.inputProps ?? undefined,
                    // disableUnderline: this.props.borderless ? true : false
                }}
                onChange={(e) => {
                    let value = e.target.value;
                    if (this.props.type === 'percent') {
                        value = value.replace(',', '.');
                        let numericValue = parseFloat(value);

                        // numericValue = Math.round(numericValue); // Arredondar para o inteiro mais próximo

                        if (numericValue > 100) numericValue = 100;
                        if (numericValue < 0) numericValue = 0;

                        e.target.value = numericValue.toString();
                    }
                    if (this.props.type === 'number') {
                        if (value.includes(',') || value.includes('.')) {
                            e.target.value = ''
                        }
                    }
                    if (this.props.type === 'currency') {
                        const maxDecimals = 2
                        const maxDigits = 9

                        value = value.replace(',', '.')

                        // Regex para limitar a 4 dígitos antes do ponto e 2 depois
                        const regex = new RegExp(`^\\d{1,${maxDigits}}(\\.\\d{0,${maxDecimals}})?`)
                        const match = value.match(regex)
                        value = match ? match[0] : ''

                        value = value.replace('.', ',')

                        e.target.value = value
                    }
                    this.props.handleChange(e)
                }}

            />
        )
    }
}

export default MainTextField