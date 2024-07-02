import React from "react";

import { Checkbox, FormControlLabel } from "@mui/material";


class MainCheckBoxInput extends React.Component {

    render() {
        return (
            <FormControlLabel
                sx={{
                    '& .MuiTypography-root': {
                        color: this.props.colors.grey[100],
                        fontSize: '16px',
                        "&.Mui-disabled": {
                            color: this.props.colors.grey[1100]
                        }
                    },
                    '& .MuiSvgIcon-root': {
                        color: this.props.colors.grey[1100]
                    },
                    ...this.props.sx,
                }}
                label={this.props.label}
                disabled={this.props.disabled ?? false}
                control={
                    <Checkbox
                        id={this.props.id}
                        checked={this.props.value === 'true' || this.props.value === true}
                        onChange={(event) => {
                            const newEvent = {
                                ...event,
                                target: {
                                    ...event.target,
                                    value: event.target.checked,
                                    id: this.props.id
                                }
                            }
                            this.props.handleChange(newEvent)
                        }}
                    />
                }
            />
        )
    }
}

export default MainCheckBoxInput