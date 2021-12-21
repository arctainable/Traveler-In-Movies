<template>
    <section>
			<div class="container">
				<div class="categorydiv">
				</div>
        <!--  -->
				<div class="listdiv">
					<div class="row" >
						<table class="col-md-4 project-item" 
            v-for="movie in movies"
            :key="movie.id" 
            :items="movies"
            :per-page="perPage"
            :current-page="currentPage">
							<div class="item-h">
								<div class="project-card">
                  <router-link :to="{ name: 'Moviedetail', params: { movie_pk:movie.id } }" >
									<div class="item-image">
										<a href="#">
											<img :src="movie.poster_path">
										</a>
									</div>
                  </router-link>
									<div class="item-funddingstat" style="height:60px; margin-top:15px; text-align:center;">
										<span class="fundding-amount">{{movie.title}}</span>
									</div>
								</div>
							</div>
						</table>
              <div class="overflow-auto">
                <b-pagination-nav :link-gen="linkGen" :number-of-pages="pageall.total_pages" align="center" use-router></b-pagination-nav>
              </div>
					</div><!-- row end -->
				</div>
			</div>
        <div class="remote-box">
          <div class="remote-box-top">퀵 메뉴</div>
          <div class="remote-box-body">
            <div title="Collapsible card" class="remote-box-sort">
              <div class="dropdown">
                <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-expanded="true"
                >
                  정렬
                </button>
                <ul class="dropdown-menu" role="menu"
                  aria-labelledby="dropdownMenu1">
                  <li role="presentation"><a role="menuitem" tabindex="-1" @click="getMovies()">번호순</a></li>
                  <li role="presentation"><a role="menuitem" tabindex="-1" @click="getRate()">평점순</a></li>
                  <li role="presentation"><a role="menuitem" tabindex="-1" @click="getPopular()">인기순</a></li>
                </ul>
              </div>
            </div>
            <div class="remote-box-all">
              <p class="procount">총 영화 <span>{{pageall.total_count}}</span></p>
            </div>
            <div class="overflow-auto remote-box-page">
              <b-pagination-nav :link-gen="linkGen" :number-of-pages="pageall.total_pages" limit='3' hide-ellipsis='true' hide-goto-end-buttons='true' align="fill" size="sm" use-router></b-pagination-nav>
            </div>
          </div>
        </div>
        <!--  -->
		</section>
</template>



<script>
import Vue from 'vue'
import axios from 'axios'
import Scrollspy from 'vue2-scrollspy'

Vue.use(Scrollspy)

export default {
  name: 'Movielist',
  data: function () {
    return {
      movies: null,
      pageall: null,
      sort: null,
    }
  },
  methods: {
    linkGen(pageNum) {
      return pageNum === 1 ? '?' : `?page_num=${pageNum}`
    },
    getMovies: function () {
      let url = 'http://127.0.0.1:8000/movies/no/'
      if (this.$route.query.page_num) {
        url += '?page_num=' + this.$route.query.page_num
      }
      axios({
        method: 'get',
        url: url,
      })
        .then(res => {
          console.log(res.data)
          this.pageall = res.data[res.data.length - 1],
          this.sort = 'all'
          res.data.pop(),
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getRate: function () {
      let url = 'http://127.0.0.1:8000/movies/rate/'
      if (this.$route.query.page_num) {
        url += '?page_num=' + this.$route.query.page_num
      }
      axios({
        method: 'get',
        url: url,
      })
        .then(res => {
          console.log(res.data)
          this.pageall = res.data[res.data.length - 1],
          this.sort = 'rate'
          res.data.pop(),
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getPopular: function () {
      let url = 'http://127.0.0.1:8000/movies/popular/'
      if (this.$route.query.page_num) {
        url += '?page_num=' + this.$route.query.page_num
      }
      axios({
        method: 'get',
        url: url,
      })
        .then(res => {
          console.log(res.data)
          this.pageall = res.data[res.data.length - 1],
          this.sort = 'popular'
          res.data.pop(),
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },

  },
  watch: {
    $route() {
      let url = null
      if (this.sort === 'all') {
        url = 'http://127.0.0.1:8000/movies/no/'
      } else if (this.sort === 'rate') {
        url = 'http://127.0.0.1:8000/movies/rate/'
      } else if (this.sort === 'popular') {
        url = 'http://127.0.0.1:8000/movies/popular/'
      }
      console.log(this.sort)
      console.log(url)
      if (this.$route.query.page_num) {
        url += '?page_num=' + this.$route.query.page_num
      }
      axios({
        method: 'get',
        url: url,
      })
        .then(res => {
          console.log(res.data)
          this.pageall = res.data[res.data.length - 1],
          res.data.pop(),
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.getMovies()
  },
  // computed: {
  //     rows() {
  //       return this.movies.length
  //     }
  //   }
}
  
</script>

<style scoped="scoped">

.remote-box {
  position:fixed; 
  width:165px; 
  height:185px; 
  border-radius: 5px;
  border:10px solid #dbdbdb;
  background: white;
  z-index:100;
  right:5%;
  top:170px;
}

.remote-box-top {
  width:100%;
  background: #474747;
  text-align: center;
  color: white;
}

.remote-box-all {
  width:100%;
  text-align: center;
  padding:5px;
}

.remote-box-sort {
  width:100%;
}

.dropdown-toggle {
  width:100%;
  background:#dbdbdb;
  border:1px solid white;
}

.remote-box-page {
  left:10;
}

/* .container {
  border:1px solid black;
} */

.user-photo{
	width:38px;
	height:38px;
	margin-right: 10px;
}

.categorydiv{
	margin:14px auto;
	width: 900px;
	text-align: center;
	
}
.categorydiv a{
	color:#555;
}
.category-part{
	display:inline-block;
	width: 80px;
	height:60px;
	font-size:13px;
	text-align:center;
	margin-right: 30px;
}
.category-1{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-2{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-3{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-4{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-5{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-6{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-7{
  display: block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}

.procount {
	font-size:16px;
}
.procount > span{
	color:#ff9696;
}

.item-h{
	margin-top:50px;
	position:relative;
}

.item-image{
	border-radius:4px;
  margin:auto;
	position:relative;
	overflow:hidden;
	width: 250px;
  height: 380px;
  border:1px solid white;
}
.item-image a img:hover{
	transform: scale(1.2);
}
.item-image a img{
	width:100%;
  height:100%;
	position:relative;
	transition:all 0.3s ease-out;
}

.item-view{
	margin-top: 15px;
  min-height: 150px;
}

.item-title {
	width:100%;
	font-size:20px;
	margin-bottom:10px; 
	overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.item-info{
	font-size: 13px;
	padding:10px;
	color:#9e9e9e;
}

.item-content{
	margin:0px 0px 16px;
	overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.wait-coment{
	text-align: center;
	border: 1px solid #dbdbdb;
	padding: 6px 0px;
	border-radius: 5px;
	color: #555;
}

.inqtext{
	resize:none;
	width: 550px;
	height:60px;
	font-size:16px;
}
.inqusend-btn a{
	display:inline-block;
	background: #ff9696;
  color: #fff;
  padding: 3px 10px;
  margin-top: 10px;
  border-radius: 5px;
}

.item-funddingstat{
	margin:0px;
	height:35px;
}
.fundding-amount{
	line-height:27px;
	color:#ff9696;
	font-size:23px;
	font-weight:700;
	margin-top:18px;
	letter-spacing:2px;
}

.fundding_contents{
	width: 300px;
  height: 145px;
  margin-top: 35px;
  background: #f6f6f6;
  padding: 20px;
}
.fundding_contents h5{
  font-size: 20px;
  color: #969696;
}
    
.fundding_contents p{
  color: #969696;
}
 
.percent{
	color:#ff9696;
	margin-left:6px;
}
.rest-day{
	margin-left:auto;
	color:#9e9e9e;
}

.mt40 {
  margin-top: 40px;
}

.mt20 {
  margin-top: 20px;
}

.user-photo {
  width: 38px;
  height: 38px;
  margin-right: 10px;
}


.sitelogo {
  width: 100%;
}

.item-funddingstat {
  margin: 0;
  height: 35px;
}

.fundding_contents {
  width: 300px;
  height: 145px;
  margin-top: 35px;
  background: #f6f6f6;
  padding: 20px;
}
.fundding_contents h5 {
  font-size: 20px;
  color: #969696;
}

.fundding_contents p {
  color: #969696;
}

.percent {
  color: #ff9696;
  margin-left: 6px;
}
.rest-day {
  margin-left: auto;
  color: #9e9e9e;
}

.project-head {
  padding-bottom: 30px;
}
.head-info {
  width: 100%;
  margin: 0 auto;
  position: relative;
  height: auto;
  padding: 0;
}
.head-title {
  height: 180px;
  padding-bottom: 0;
  align-items: center;
  justify-content: center;
}
.title-div {
  text-align: center;
  margin: 0 auto;
  padding: 10px;
  margin-top: 50px;
}

.projectimg {
  width: 100%;
}
.fundding-info {
  padding: 0 15px 30px 45px;
}

.fundding-stat {
  font-size: 14px;
  font-weight: 700;
}
.info-text {
  font-size: 14px;
  min-width: 70px;
  line-height: 30px;
  display: inline-block;
  color: #969696;
}
.info-now {
  font-size: 20px;
}
.info-goal {
  font-size: 12px;
  color: #969696;
  line-height: 28px;
}

.btn-warp {
  width: 100%;
}
.btn-warp a {
  display: inline-block;
  padding: 8px 14px;
  border: 1px solid #dbdbdb;
}
.like-btn {
  display: inline-block;
  padding: 8px 14px;
  border: 1px solid #dbdbdb;
  color: #ff9696;
  background: #fff;
}
.project-bar {
  border-top: 1px solid #dbdbdb;
  border-bottom: 1px solid #dbdbdb;
  box-shadow: rgb(0 0 0 / 10%) 0 2px 3px;
}
.project-bar div a {
  display: inline-block;
  font-size: 14px;
  padding: 20px;
}

.content-section {
  background: #f6f6f6;
}

.project-content,
.reward-list,
.writer-info {

  padding: 30px;
  background: #fff;
  border: 1px solid #dbdbdb;
}

.project_content_image {
  width: 630px;
}

.project-content img {
  max-width: 100%;
}

.project-content {
  margin-bottom: 60px;
}
.community-card {
  position: relative;
}
.community-card-head {
  vertical-align: bottom;

}
.commu-write {
  display: inline-block;
  vertical-align: -12px;
}
.community-card-body {
  min-height: 30px;
  max-height: 500px;
  overflow: hidden;
}
.commu-content {
  padding: 21px 0;
}
.gmflrp {
  position: absolute;
  display: block;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  z-index: 200;
  background: linear-gradient(rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.5) 45%, rgb(255, 255, 255));
  content: "";
}
.more-content {
  width: 100%;
}
.more-content a {
  border-radius: 5px;
  padding: 10px;
  display: inline-block;
  width: 100%;
  text-align: center;
  background: rgba(255,150,150,0.2);
  font-weight: 700;
}

.community-card-foot {
  width: 100%;
  padding-top: 10px;
  border-top: 1px solid #dbdbdb;
}

.comment-inbox {
  position: relative;
  margin-bottom: 10px;
}

.user-comment {
  border-bottom: 1px solid #dbdbdb;
  padding-bottom: 20px;
}

.comment-inbox-name {
  display: block;
  margin-bottom: 10px;
  font-weight: 500;
  font-size: 13px;
}

.comment-inbox-text {
  overflow: hidden;
  min-height: 17px;
  width: 100%;
  border: 0;
  font-size: 13px;
  resize: none;
}

.comment-writer {
  margin: 12px 0 29px;
  padding: 16px 10px 10px 18px;
  border: 1px solid #efefef;
  border-radius: 3px;

}
.comment-delete-btn {
  display: inline-block;
  background: #ff9696;
  color: #fff;
  padding: 1px 5px;
  border-radius: 5px;
}
.commu-write {
  margin-bottom: 20px;
}

.rmfTmrldiv span {
  margin-left: 10px;
  margin-top: 10px;
  display: inline-block;
}

.button_p {
  color: #fff;
  background: #FF9696;
  border: none;
  padding: 10px 50px;
  margin: 10px;
  font-size: 17px;
}

.register-btn {
  color: #FF9696;
  background: #ffffff;
  border: 1px solid #FF9696;
  padding: 15px 40px;
  margin: 20px 0;
  font-size: 16px;
  display: inline-block;
}

.community_wb {
  color: #fff;
  background: #FF9696;
  border: none;
  padding: 10px 20px;
  margin: 10px;
  font-size: 15px;
}

.community_b a {
  border: 1px solid #dbdbdb;
  padding: 10px;
}

.comment_b {
  border: 1px solid #FF9696;
  padding: 5px 10px;
  color: #FF9696;
}

.s-size-photo {
  height: 150px;
  margin-right: 30px;
}

.order-check {
  border-top: 1px solid #dbdbdb;
  padding: 24px;
}

.order-state-head {
  font-size: 16px;
  color: #333;
  font-weight: 500;
}
.order-state-body input {
  border: 1px solid #dbdbdb;
  height: 35px;
}
.order-state-body {
  border: 1px solid #dbdbdb;
  border-radius: 5px;
  padding: 10px;
}

.precautions {
  font-size: 11px;
  padding: 8px;
}

.order-last-pay div:first-child {
  color: #ff9696;
  font-size: 16px;
}

.order-state-table tr th {
  padding: 4px 0 4px 20px;
  vertical-align: top;
  text-align: left;
}

.order-state-text {
  padding: 4px 0 4px 20px;
  font-size: 12px;
}

.order-state-table {
  width: 100%;
  margin: 16px 0;
}

.order-last-pay {
  padding: 10px;
}

.perinfo-check div a {
  margin: 3px 0 0 10px;
  display: inline-block;
  color: #27a3ff;
  text-decoration: underline;
}

.more-info {
  margin: 3px 0 0 10px;
}

.project-order-submit a {
  display: inline-block;
  background: #ff9696;
  color: #fff;
  font-size: 16px;
  border-radius: 3px;
  padding: 10px 30%;
}

.project-order-submit {
  text-align: center;
}
.precautions span {
  color: #ff9696;
  font-weight: 700;
}

.order-complete {
  text-align: center;
}

.congratu {
  margin-top: 100px;
  color: #ff9696;
}

.postNum_b {
  background: #f6f6f6;
  color: #969696;
  padding: 10px;
  border: none;
}

.mainBack_button {
  color: #FF9696;
  background: #ffffff;
  border: 1px solid #FF9696;
  padding: 15px 60px;
  margin: 20px;
  font-size: 16px;
  display: inline-block;
  margin-bottom: 100px;
}

.project_list_button {
  background: #FF9696;
  border: none;
  padding: 15px 50px;
  margin: 20px;
  font-size: 16px;
}

.xpdlqmf {
  text-align: center;
}

.fundding-amount1 {
  line-height: 27px;
  color: #ff9696;
  font-size: 25px;
  font-weight: 700;
  margin-top: 18px;
  letter-spacing: 2px;
}

.order_radio_b {
  height: 13px;
  margin-right: 10px;
  margin-left: 100px;
}
.item-image a img{
  width:100%;
}
</style>