import React from "react";

import { ColorPicker } from 'mui-color';

class MainColorInput extends React.Component {
    constructor(props) {
        super(props)
        
    }

    handleChangeDate = (color) => {
            const event = {
                target: {
                    id: this.props.id,
                    value: `#${color.hex}`
                }
            }
        this.props.handleChange(event)
    }

    render () {
        return (
            <ColorPicker 
                value={this.props.value} 
                inputFormats={['hex', 'rgb']} 
                hideTextfield={true}
                onChange={(color) => this.handleChangeDate(color)} 
            />
        )
    }
}

export default MainColorInput;