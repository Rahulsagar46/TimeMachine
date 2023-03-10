import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import getMonthFromIndex from '../../helper';

const LeftSubcomponent = ({ initialinfo, setInitialinfo }) => {
    const columns = [
        { field: 'col1', headerName: 'Date', width: 110 },
        { field: 'col2', headerName: 'Day', width: 110 },
        { field: 'col3', headerName: 'Total Working time (hrs)', width: 130 },
        { field: 'col4', headerName: 'Net Working time', width: 130}
      ];
      const rows = initialinfo["log_entries"] === undefined ? [] : initialinfo["log_entries"].map((row) => ({
          id   : initialinfo["log_entries"].indexOf(row), 
          col1 : row["date"],
          col2 : row["week_day"],
          col3 : row["total_work_time_for_day"],
          col4 : '-00:30'
      }));
    const dateObj = new Date();
    const currentYear = dateObj.getFullYear();
    const currentMonth = getMonthFromIndex(dateObj.getMonth());
    return (
        <div className='LeftSubcomponent'>
            <div className='LeftSubBanner'>
                <div className="dropdown">
                        <button className="dropbtn">{currentMonth}</button>
                        <div className="dropdown-content">
                            <a href="#">January</a>
                            <a href="#">February</a>
                            <a href="#">March</a>
                            <a href="#">April</a>
                            <a href="#">May</a>
                            <a href="#">June</a>
                            <a href="#">July</a>
                            <a href="#">August</a>
                            <a href="#">September</a>
                            <a href="#">October</a>
                            <a href="#">November</a>
                            <a href="#">December</a>
                        </div>
                </div>
                <div className="dropdown">
                    <button className="dropbtn">{currentYear}</button>
                    <div className="dropdown-content">
                        <a href="#">2023</a>
                        <a href="#">2022</a>
                    </div>
                </div> 
            </div>
            <div className='DataGridContainer'>
                { initialinfo["log_entries"] !== undefined ? <DataGrid rows={rows} columns={columns} rowHeight={30} /> : null }
            </div>
        </div>
    );
}

export default LeftSubcomponent