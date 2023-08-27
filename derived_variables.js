function evaluateBucketing(logic, response) {
    let res = null;
    switch(logic.fieldType) {
      case 'ques': {
        if(response.resAObj && logic.fieldId.id && response.resAObj[logic.fieldId.id]) {
          let resAObj = response.resAObj[logic.fieldId.id];
          for(let i = 0; i < logic.domain.length; i++) {
            let map = logic.mapping[logic.domain[i]];
            for(let j = 0; j < map.length; j++) {
              let idx = resAObj.findIndex((resp) => { return isObjectEquivalentForBucketing(resp, map[j]) });
              if(idx > -1) {
                res = logic.domain[i];
                break;
              }
            }
            if(res) {
              break;
            }
          }
        }
        break;
      }
      case 'eData': {
        if(response.eData && logic.fieldId.id && response.eData[logic.fieldId.id]) {
          for(let i = 0; i < logic.domain.length; i++) {
            let map = logic.mapping[logic.domain[i]];
            let idx = map.indexOf(response.eData[logic.fieldId.id]);
            if(idx > -1) {
              res = logic.domain[i];
              break;
            }
          }
        }
        break;
      }
      case 'agents': {
        if(response.agent) {
          for(let i = 0; i < logic.domain.length; i++) {
            let map = logic.mapping[logic.domain[i]];
            let idx = map.indexOf(response.agent);
            if(idx > -1) {
              res = logic.domain[i];
              break;
            }
          }
        }
        break;
      }
    }
    return res;
  }
  
  function isObjectEquivalentForBucketing(resp, map) {
    if(typeof(resp) != 'object' || typeof(map) != 'object') {
      return false;
    }
    if(map['rowId']) {
      if(map['rowId'] != resp['rowId']) {
        return false;
      }
    }
    if(map['colId']) {
      if(map['colId'] != resp['colId']) {
        return false;
      }
    }
    if(map['itemId']) {
      if(map['itemId'] != resp['itemId']) {
        return false;
      }
    }
    return true;
  }