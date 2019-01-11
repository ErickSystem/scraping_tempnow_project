export function mergeData(primary, secundary, primaryDetail, secundaryDetail) {
    const indexed = {}
    for(const e of primary){
      indexed[e.id] = {
        establishment: {
          city: e.city,
          companyName: e.companyName,
          establishmentName: e.establishmentName,
          id: e.id,
          isMall: e.isMall,
          stateName: e.stateName
        },
        primary: e.data,
      }
    }
  
    if (secundary) {
      for(const e of secundary){
        indexed[e.id].secundary = e.data
      }
    }
  
    if (primaryDetail) {
      for(const e of primaryDetail) {
        const indexedDetail = indexed[e.id].detail = {}
        for(const d of e.data) {
          indexedDetail[d.key] = {
            calendar: d.calendar,
            date: d.key,
            key: d.key,
            primary: d.value
          }
        }
      }
    }
  
    
  
    if (secundaryDetail) {
      for(const e of secundaryDetail) {
        const indexedDetail = indexed[e.id].detail
        for(const d of e.data) {
          indexedDetail[d.key].secundary = d.value
        }
      }
    }
  
    return indexed;
  }
  
  export function mergeDataWithDevice(primary, secundary, primaryDetail, secundaryDetail) {
    const indexed = {}
    for(const e of primary){
      indexed[e.id] = {
        establishment: {
          city: e.city,
          companyName: e.companyName,
          establishmentName: e.establishmentName,
          id: e.id,
          isMall: e.isMall,
          stateName: e.stateName
        },
        primary: e.data,
      }
    }
  
    if (secundary) {
      for(const e of secundary){
        indexed[e.id].secundary = e.data
      }
    }
  
    if (primaryDetail) {
      for(const e of primaryDetail) {
        const indexedDetail = indexed[e.id].detail = {}
        for(const d of e.data) {
          indexedDetail[d.key] = {
            calendar: d.calendar,
            date: d.key,
            key: d.key,
            primary: d.value
          }
        }
      }
    }
  
    if (secundaryDetail) {
      for(const e of secundaryDetail) {
        const indexedDetail = indexed[e.id].detail
        for(const d of e.data) {
          indexedDetail[d.key].secundary = d.value
        }
      }
    }
  
    return indexed;
  }
  
  export function mergeDataByDevice(primary, secundary, primaryDetail, secundaryDetail) {
    const indexed = {}
    for(const e of primary){
      indexed[e.id] = {
        establishment: {
          city: e.city,
          companyName: e.companyName,
          establishmentName: e.establishmentName,
          id: e.id,
          isMall: e.isMall,
          stateName: e.stateName,
          devices: {},
        },
        primary: 0
      }
  
      const establishment = indexed[e.id].establishment
  
      for(const peek of e.data) {
        establishment.devices[peek.id] = {
          deviceName: peek.description,
          id: peek.id,
          primary: peek.data
        }
  
        indexed[e.id].primary += peek.data
      }
    }
  
    if (secundary) {
      for(const e of secundary){
        if(!indexed[e.id]) {
          indexed[e.id] = {
            establishment: {
              city: e.city,
              companyName: e.companyName,
              establishmentName: e.establishmentName,
              id: e.id,
              isMall: e.isMall,
              stateName: e.stateName,
              devices: {},
            }
          }
        }
  
        const establishment = indexed[e.id].establishment
  
        indexed[e.id].secundary = 0
  
        for(const peek of e.data) {
          if (!establishment.devices[peek.id]) {
            establishment.devices[peek.id] = {
              deviceName: peek.description,
              id: peek.id
            }
          }
          establishment.devices[peek.id].secundary = peek.data
  
          indexed[e.id].secundary += peek.data
        }
      }
    }
  
    if (primaryDetail) {
      for(const e of primaryDetail) {
        for(const peek of e.data){
          const indexedDetail = indexed[e.id].establishment.devices[peek.id].detail = {}
          for(const d of peek.data) {
            indexedDetail[d.key] = {
              calendar: d.calendar,
              date: d.key,
              key: d.key,
              primary: d.value
            }
          }
        }
      }
    }
  
    if (secundaryDetail) {
      for(const e of secundaryDetail) {
        for(const peek of e.data){
          if(!indexed[e.id].establishment.devices[peek.id].detail)
            indexed[e.id].establishment.devices[peek.id].detail = {}
          
          const indexedDetail = indexed[e.id].establishment.devices[peek.id].detail
          for(const d of peek.data) {
            indexedDetail[d.key] = {
              calendar: d.calendar,
              date: d.key,
              key: d.key,
              secundary: d.value
            }
          }
        }
      }
    }
  
    return indexed;
  }
  
  export function mergeDataByAmbient(primary, secundary, primaryDetail, secundaryDetail) {
    const indexed = {}
    for(const e of primary){
      indexed[e.id] = {
        establishment: {
          city: e.city,
          companyName: e.companyName,
          establishmentName: e.establishmentName,
          id: e.id,
          isMall: e.isMall,
          stateName: e.stateName,
          ambients: {},
        },
        primary: 0
      }
  
      const establishment = indexed[e.id].establishment
  
      for(const ambient of e.data) {
        establishment.ambients[ambient.id] = {
          ambientName: ambient.ambientName,
          id: ambient.id,
          primary: ambient.data
        }
  
        indexed[e.id].primary += ambient.data
      }
    }
  
    if (secundary) {
      for(const e of secundary){
        if(!indexed[e.id]) {
          indexed[e.id] = {
            establishment: {
              city: e.city,
              companyName: e.companyName,
              establishmentName: e.establishmentName,
              id: e.id,
              isMall: e.isMall,
              stateName: e.stateName,
              ambients: {},
            }
          }
        }
  
        const establishment = indexed[e.id].establishment
  
        indexed[e.id].secundary = 0
  
        for(const ambient of e.data) {
          if (!establishment.ambients[ambient.id]) {
            establishment.ambients[ambient.id] = {
              ambientName: ambient.ambientName,
              id: ambient.id
            }
          }
          establishment.ambients[ambient.id].secundary = ambient.data
  
          indexed[e.id].secundary += ambient.data
        }
      }
    }
  
    if (primaryDetail) {
      for(const e of primaryDetail) {
        for(const ambient of e.data){
          const indexedDetail = indexed[e.id].establishment.ambients[ambient.id].detail = {}
          for(const d of ambient.data) {
            indexedDetail[d.key] = {
              calendar: d.calendar,
              date: d.key,
              key: d.key,
              primary: d.value
            }
          }
        }
      }
    }
  
    if (secundaryDetail) {
      for(const e of secundaryDetail) {
        for(const ambient of e.data){
          if(!indexed[e.id].establishment.ambients[ambient.id].detail)
            indexed[e.id].establishment.ambients[ambient.id].detail = {}
          
          const indexedDetail = indexed[e.id].establishment.ambients[ambient.id].detail
          for(const d of ambient.data) {
            indexedDetail[d.key] = {
              calendar: d.calendar,
              date: d.key,
              key: d.key,
              secundary: d.value
            }
          }
        }
      }
    }
  
    return indexed;
  }
  
  export function indexedToDataView(indexed, order, detailKeyFormater) {
  
    const data = Object.values(indexed).filter(x => x.primary != null || x.secundary != null)
    
    let orderFn = (a, b) => a.establishment.establishmentName.localeCompare(b.establishment.establishmentName);
    if(order === 'primary')
      orderFn = (a, b) => a.primary - b.primary
    if(order === 'secundary')
      orderFn = (a, b) => a.secundary - b.secundary
  
    data.sort(orderFn)
  
    if(detailKeyFormater) {
      for(const e of data) {
        if(e.detail) {
          e.detail = Object.values(e.detail).filter(x => x.primary != null || x.secundary != null).sort(compareByKey)
          for(const d of e.detail)
             d.key = detailKeyFormater(d.key)
        }
        if(e.establishment.devices) {
          try {
            
            e.establishment.devices = Object.values(e.establishment.devices).filter(x => x.primary != null || x.secundary != null)
            
            e.establishment.devices.sort((a, b) => a.deviceName.localeCompare(b.deviceName))
            
            for(const dv of e.establishment.devices) {
              if(dv.detail) {
                dv.detail = Object.values(dv.detail).filter(x => x.primary != null || x.secundary != null).sort(compareByKey)
                for(const d of dv.detail)
                  d.key = detailKeyFormater(d.key)
              }
            }
          } catch(e) {
            console.log("WARNING!!!", e)
          }
        }
        if(e.establishment.ambients) {
          try {
            
            e.establishment.ambients = Object.values(e.establishment.ambients).filter(x => x.primary != null || x.secundary != null)
            
            e.establishment.ambients.sort((a, b) => a.ambientName.localeCompare(b.ambientName))
            
            for(const am of e.establishment.ambients) {
              if(am.detail) {
                am.detail = Object.values(am.detail).filter(x => x.primary != null || x.secundary != null).sort(compareByKey)
                for(const d of am.detail)
                  d.key = detailKeyFormater(d.key)
              }
            }
          } catch(e) {
            console.log("WARNING!!!", e)
          }
        }
      }
    }
  
    return data
  }
  
  
  function compareByKey(a, b) {
    if (a.key < b.key)
      return -1;
    if (a.key > b.key)
      return 1;
    return 0;
  }
  
  export function zip(first, ...others) {
    return first.map((v, i) => [v, ...others.map(l => l && l[i])])
  }
  