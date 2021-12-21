import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate" // 프로필에서 새로고침 시 다 날라감 ~ 개인 브라우저의 경우는 로컬에 저장하는게 편할듯

Vue.use(Vuex)

import axios from 'axios'
import swal from "sweetalert";
import SERVER from '@/api/server.js'

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    jwtToken: localStorage.getItem("jwt"),
    nickname: '',
    profile_image: '',
    background_image: '',
    rank_point: null,
    userid : null,
    genres_cnt: {},
    countries_cnt: {},
    reviews: [],
    review_movies: [],
    review_movies_genre: [],
    review_movies_country: [],
    hover_idx: 0,
    usernamei: localStorage.getItem("username")
  },
  getters: {
    config: function (state) {
      return {
        Authorization: `JWT ${state.jwtToken}`,
      }
    },
    getUserid: function (state) {
      return {
        userid: state.userid
      }
    },
    getusernamei: state => {
      return state.usernamei
    }
  },

  mutations: {
    INIT_DATA: function (state) {
      state.jwtToken = localStorage.getItem("jwt"),
      state.nickname = '',
      state.profile_image = '',
      state.background_image = '',
      state.rank_point = null,
      state.userid  = null,
      state.genres_cnt = {},
      state.countries_cnt = {},
      state.reviews = [],
      state.review_movies = [],
      state.review_movies_genre = [],
      state.review_movies_country = [],
      state.hover_idx = 0,
      state.usernamei = localStorage.getItem("username")
    },
    LOGIN_GET_TOKEN: function (state) {
      state.jwtToken = localStorage.getItem("jwt")
    },
    GET_PROFILE: function (state, data) {
      state.userid = data.userid
      state.nickname = data.nickname
      state.profile_image = data.profile_image
      state.background_image = data.background_image
      state.rank_point = data.rank_point
    },
    GET_REVIEWS_GENRE: function (state, data) {
      state.genres_cnt = data
    },
    GET_REVIEWS_COUNTRY: function (state, data) {
      state.countries_cnt = data
    },
    GET_REVIEWS: function (state, data) {
      state.reviews = data
    },
    GET_REVIEWS_MOVIE_INFO: function (state, data) {
      state.review_movies = data
    },
    RANKPOINT_UPDATE: function (state, data) {
      state.rank_point = data.rank_point
    },
    GET_REVIEWS_MOVIE_GENRE_COUNTRY: function (state, data) {
      state.review_movies_genre = data.genre
      state.review_movies_country = data.country
    },
  },
  actions: {
    initData: function ({commit}) {
      commit("INIT_DATA")
    },
    loginGetToken: function ({commit}) {
      commit("LOGIN_GET_TOKEN")
    },

    getProfile: function ({commit, getters}) {
      axios({
        method: "get",
        url: `${SERVER.URL}/accounts/profile/`,
        headers: getters.config,
      })
        .then( res => {
          const userid = res.data.id
          const nickname = res.data.nickname
          const profile_image = `${SERVER.URL}` + res.data.profile_image
          const background_image = `${SERVER.URL}` + res.data.background_image
          const rank_point = res.data.rank_point
          commit("GET_PROFILE", {userid, nickname, profile_image, background_image, rank_point})
        })
        .catch( err => {
          console.log(err)
        })
    },
    profileUpdate: function ({commit, getters}, credentials) {
      axios({
        method: "put",
        url: `${SERVER.URL}/accounts/profile/`,
        data: credentials,
        headers: getters.config,

      })
        .then( res => {
          const nickname = res.data.nickname
          const profile_image = `${SERVER.URL}` + res.data.profile_image
          const background_image = `${SERVER.URL}` + res.data.background_image
          const rank_point = res.data.rank_point
          const username = res.data.username
          commit("GET_PROFILE", {username, nickname, profile_image, background_image, rank_point})
        })
        .catch( err => {
          swal(err.response.data.error, {
            dangerMode: true,
          })
        })

    },
    getReviewsGenre: function ({commit, getters}) {

      setTimeout(() => {
        axios({
          method: "get",
          url: `${SERVER.URL}/accounts/profile/${getters.getUserid.userid}/reviews/genre/`,
          headers: getters.config,
          
        })
          .then( res => {
            commit("GET_REVIEWS_GENRE", res.data)
          })
          .catch( err => {
            console.log(err)
          })
      }, 0)
    
    },
    getReviewsCountry: function ({commit, getters}) {

      setTimeout(() => {
        axios({
          method: "get",
          url: `${SERVER.URL}/accounts/profile/${getters.getUserid.userid}/reviews/country/`,
          headers: getters.config,
        })
          .then( res => {
            commit("GET_REVIEWS_COUNTRY", res.data)
          })
          .catch( err => {
            console.log(err)
          })
      },0)
    },
    getReviews: function ({commit, getters}) {
      setTimeout(() => {
        axios({
          method: "get",
          url: `${SERVER.URL}/accounts/profile/${getters.getUserid.userid}/reviews/`,
          headers: getters.config,
        })
          .then( res => {
            commit("GET_REVIEWS", res.data)
          })
          .catch( err => {
            console.log(err)
          })
        },0)
    },
    getReviewsMovieInfo: function ({commit, getters}) {
      setTimeout(() => {
        axios({
          method: "get",
          url: `${SERVER.URL}/accounts/profile/${getters.getUserid.userid}/reviews/movies/`,
          headers: getters.config,
        })
          .then( res => {
            commit("GET_REVIEWS_MOVIE_INFO", res.data)
          })
          .catch( err => {
            console.log(err)
          })
        }, 0)
    },
    userRankpointUpdate: function ({commit, getters}, formdata) {
      axios({
        method: "put",
        url: `${SERVER.URL}/accounts/profile/`,
        data: formdata,
        headers: getters.config,

      })
        .then( res => {
          commit("RANKPOINT_UPDATE", res.data)
        })
        .catch( err => {
          swal(err.response.data.error, {
            dangerMode: true,
          })
        })
    },
    getReviewsMovieGenreCountry: function ({commit, getters}) {
      setTimeout(() => {
        axios({
          method: "get",
          url: `${SERVER.URL}/accounts/profile/${getters.getUserid.userid}/reviews/genre_country_movies/`,
          headers: getters.config,
        })
          .then( res => {
            commit("GET_REVIEWS_MOVIE_GENRE_COUNTRY", res.data)
          })
          .catch( err => {
            console.log(err)
          })
        },0)
    },
  },
  modules: {
  }
})
