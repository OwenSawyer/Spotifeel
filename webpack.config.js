var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    //the base directory (absolute path) for resolving the entry option
    context: __dirname,
    //the entry point we created earlier. Note that './' means 
    //your current directory. You don't have to specify the extension now,
    //because you will specify extensions later in the `resolve` section
    entry: [
        'react-hot-loader/patch',
        'webpack-dev-server/client?http://localhost:3000',
        'webpack/hot/only-dev-server',
        './assets/app'
    ],
    output: {
        //where you want your compiled bundle to be stored
        path: path.resolve('./assets/bundles/'),
        publicPath: 'http://localhost:3000/assets/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
        //naming convention webpack should use for your files
        filename: '[name]-[hash].js',
    },

    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin(), // don't reload if there is an error
        new BundleTracker({filename: './webpack-stats.json'}),
    ],

    module: {
        rules: [
            //a regexp that tells webpack use the following loaders on all
            //.js and .jsx files
            {
                test: /\.jsx?$/,
                //we definitely don't want babel to transpile all the files in
                //node_modules. That would take a long time.
                exclude: /node_modules/,
                use: [
                    {
                        loader: "react-hot-loader/webpack",
                    },
                    {
                        loader: "babel-loader",
                        query: {
                            //specify that we will be dealing with React code
                            presets: [['es2015', { modules: false }], 'react']
                        }
                    }
                ]
            },
            // the next regex tells webpack to use style-loader and css-loader
            // (notice the chaining through the '!' syntax)
            // on all css files
            {
                test: /\.css$/,
                loader: ['style-loader', 'css-loader']
            },
            {
                test: /\.png$/,
                use: [{
                        loader: "url-loader",
                        options: {
                            limit: 100000
                        }
                }]
            },
            {
                test: /\.jpg$/,
                use: [{
                        loader: "url-loader",
                        options: {
                            limit: 100000
                        }
                }]
            },
            {
                test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
                use: [{
                        loader: "url-loader",
                        options: {
                            limit: 100000,
                            mimetype: 'application/font-woff'
                        }
                }]
            },
            {
                test: /\.tff(\?v=\d+\.\d+\.\d+)?$/,
                use: [{
                        loader: "url-loader",
                        options: {
                            limit: 100000,
                            mimetype: 'application/octet-stream'
                        }
                }]
            },
            {
                test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
                use: 'file-loader'
            },
            {
                test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
                use: [{
                        loader: "url-loader",
                        options: {
                            limit: 100000,
                            mimetype: 'image/svg+xml'
                        }
                }]
            },
        ]
    },

    resolve: {
        //tells webpack where to look for modules
        modules: ['node_modules'],
        //extensions that should be used to resolve modules
        extensions: ['.js', '.jsx']
    }
};
