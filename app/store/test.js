import shop from '@/api/shop'
import api from '@/api/api'
import axios from 'axios';

const state = {
  all: []
}

const actions = {
  getAllSongs ({commit}) {
    return axios({
        method: "POST",
        "url": "http://localhost:8000/api/user/test/",
        "data": {'token': this.token},
        "headers": { "content-type": "application/json" }
    }).then(response => {
      // JSON responses are automatically parsed.
        commit('recieve_songs', response.data)
        alert("hello")
      })
      .catch(e => {
        this.errors.push(e)
        alert("hello2")
      })

    // return api.post('http://127.0.0.1:8000/api/user/test/', {'token': token})
    //     .then((response) => Promise.resolve(response))
    //       commit('recieve_songs', songs)
    //     })
  }
}

const mutations = {
  recieve_songs (state, songs) {
    state.all = songs
  }
}

const getters = {
  allSongs (state) {
    return state.all
  }
}

export default {
  state,
  actions,
  mutations,
  getters
}
