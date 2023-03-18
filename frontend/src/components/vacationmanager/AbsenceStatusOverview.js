import React from 'react';
import {useState} from 'react';
import { DataGrid } from '@mui/x-data-grid';

const AbsenceStatusOverview = () => {
    const [activeSideTab, setActiveSideTab] = useState("planned")
    console.log(activeSideTab)
    const columns = [
        { field: 'col1', headerName: 'From', width: 95, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col2', headerName: 'To', width: 95, headerAlign:'center', headerClassName:'DataGridCols' },
        { field: 'col3', headerName: 'Total', width: 95, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col4', headerName: 'Status', width: 95, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col5', headerName: 'Action', width: 200, headerAlign:'center', headerClassName:'DataGridCols'},
      ];
    const rows = [];
    return (
        <div className='AbsenceStatusOverviewContainer'>
            <div className='SubSideNav'>
                <div className={activeSideTab === "planned" ? 'SubSideNavItem SubSideNavItemActive' : 'SubSideNavItem SubSideNavItemInactive'} onClick={() => {setActiveSideTab("planned")}}> Planned </div>
                <div className={activeSideTab === "applied" ? 'SubSideNavItem SubSideNavItemActive' : 'SubSideNavItem SubSideNavItemInactive'} onClick={() => {setActiveSideTab("applied")}}> Applied </div>
            </div>
            <div className='AbsenceStatusDatagridContainer'>
                <DataGrid checkboxSelection rows={rows} columns={columns} rowHeight={30} />
            </div>
        </div>
    )
}

export default AbsenceStatusOverview