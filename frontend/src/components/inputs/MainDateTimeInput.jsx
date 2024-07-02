import React from "react";

import dayjs from 'dayjs';
import timezone from 'dayjs/plugin/timezone';
import utc from 'dayjs/plugin/utc';

import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import { TextField } from "@mui/material";

dayjs.extend(utc);
dayjs.extend(timezone);

class MainDateTimeInput extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            sxParams: {
                '& label.Mui-focused': {
                    color: this.props.colors.blueAccent[400],
                },
                '& label': {
                    color: this.props.colors.grey[1100],
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
                }
            }
        }
    }

    componentWillMount() {
        var css = this.state.sxParams
        if (this.props.type === 'time') {
            if (this.props.borderless) {
                css = Object.assign({},
                    {
                        '& .MuiInput-root': {
                            borderBottom: `0.5px solid ${this.props.colors.grey[1100]}`,
                            color: this.props.colors.grey[100],
                            padding: '1px 2px',
                            fontSize: '14px',
                            marginRight: '20px'
                        },
                        '& .MuiInput-input': {
                            padding: '0'
                        },
                        width: this.props.fullWidth ? '93%' : '90%'
                    },
                    css)
            } else {
                css = Object.assign({},
                    {
                        input: {
                            color: this.props.colors.grey[100]
                        },
                        '& .MuiInputBase-input.Mui-disabled': {
                            WebkitTextFillColor: this.props.colors.grey[100],
                            opacity: 0.7
                        },
                        label: {
                            "&.Mui-disabled": {
                                color: this.props.colors.grey[1100]
                            }
                        },
                        width: this.props.width ? this.props.width : this.props.fullWidth ? '97%' : '94%'
                    },
                    css)
            }
        }

        this.setState({
            sxParams: css
        })
    }

    handleChange = (event) => {
        if (this.props.type === 'time') {
            const timeRegex = /^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/

            if (!event.target.value || timeRegex.test(event.target.value)) {
                this.setState({ errorMessage: '' })
            } else {
                this.setState({ errorMessage: 'Hora Incorreta' })
            }

            this.props.handleChange(event)
        }
    }

    handleChangeDate = (date) => {
        if (this.props.onlyDate) {                                                  // caso o campo esteja como "date" no banco
            var formattedDate = date ? dayjs(date).format('YYYY-MM-DD') : '';
        } else {                                                                    // caso o campo esteja como "datetime" no banco
            var formattedDate = date
        }

            const event = {
                target: {
                    id: this.props.id,
                    value: formattedDate
                }
            }
        this.props.handleChange(event)
    }

    render() {
        if (this.props.type === 'time') {
            return (
                <>
                    <TextField
                        id={this.props.id ?? undefined}
                        sx={this.state.sxParams}
                        variant={this.props.borderless ? 'standard' : 'outlined'}
                        disabled={this.props.disabled ?? false}
                        multiline={this.props.minRows ? true : false}
                        rows={this.props.minRows ?? 1}
                        value={this.props.value ?? undefined}
                        label={this.props.label ?? ''}
                        size={this.props.size ?? 'small'}
                        fullWidth={this.props.fullWidth ? true : false}
                        placeholder={this.props.type === 'time' ? 'hh:mm' : ''}
                        onChange={(e) => this.handleChange(e)}
                        InputProps={{
                            endAdornment: this.props.inputProps ?? undefined,
                        }}
                    />
                    <div style={{ color: this.props.colors.redAccent[500], fontWeight: 'bold' }} >{this.state.errorMessage}</div>
                </>
            )
        } else if (this.props.type === 'date') {
            return (
                <LocalizationProvider dateAdapter={AdapterDayjs} >
                    <DatePicker
                            sx={{
                            input: {
                                color: this.props.colors.grey[200],
                            },
                            '& .MuiInputBase-root.Mui-disabled': {
                                backgroundColor: this.props.colors.primary[400],
                            },
                            '& .MuiInputBase-input.Mui-disabled': {
                                WebkitTextFillColor: this.props.colors.grey[100],
                                
                                opacity: 0.7,
                            },
                            '& .MuiSvgIcon-root': {
                                color: this.props.colors.grey[1100]
                            },
                            '& .MuiInputBase-root': {
                                height: '40px'
                            },
                            '& .MuiOutlinedInput-root': {
                                '& fieldset': {
                                    borderColor: this.props.colors.grey[1100],
                                },
                                '&.Mui-focused fieldset': {
                                    borderColor: this.props.colors.blueAccent[400],
                                },
                            },
                            label: {
                                "&.Mui-disabled": {
                                    color: this.props.colors.grey[1100],
                                    
                                }
                            },
                            width: this.props.width ? this.props.width : this.props.fullWidth ? '97%' : '94%',
                        }}
                        label={this.props.label ?? ''}
                        disabled={this.props.disabled ?? false}
                        value={dayjs(this.props.value).tz('Etc/UTC') ?? undefined}
                        format="DD/MM/YYYY"
                        onChange={(date) => this.handleChangeDate(date)}
                    />
                </LocalizationProvider>
            )
        }
    }
}

export default MainDateTimeInput