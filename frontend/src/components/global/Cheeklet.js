import React from 'react';

const Cheeklet = ({cheeklet_header, cheeklet_val}) => { 
    return (
            <div className='Cheeklet'>
                <div className='CheekletHeader'>{cheeklet_header}</div>
                <div className='TimeVal'>{cheeklet_val}</div>
            </div>
    );
}

export default Cheeklet