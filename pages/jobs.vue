<template>
    <section>
        <ul style="list-style-type: none;">
            <li v-for="school in schools" :key=school.school>
                <v-card>
                    <v-container style="padding: 0">
                        <v-layout row>
                            <v-flex xs4>
                                <v-img 
                                class="white--text"                                
                                :src=school.imageUrl
                                >
                                </v-img>
                            </v-flex>
                            <v-flex xs8>
                                <v-card-title>
                                <div>
                                    <span class="grey--text">Published: {{school.pub_date}}</span><br>
                                    <span>{{school.school}}</span><br>
                                    <span>Blah blah blah</span>
                                </div>
                                </v-card-title>
                                <v-card-actions>
                                    <v-btn flat color="orange">View</v-btn>
                                </v-card-actions>
                            </v-flex>
                        
                        </v-layout>
                    </v-container>
                </v-card>
            </li>
        </ul>
    </section>
</template>


<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data () {
    return {
      schools: ''
    }
  },
  methods: {
    getSchools () {
      const path = 'https://rufusbrown.pythonanywhere.com/api/getSchools'
      axios.get(path)
        .then((res) => {
          console.log('response:', res.data)
          this.schools = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    }
  },
  created () {
    this.getSchools()
  }
}
</script>