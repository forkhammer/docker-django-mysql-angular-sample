var path = require('path');
var webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
var CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
    entry: [
        "bootstrap-webpack!./static/src/bootstrap.config.js",
        './static/src/app.coffee'
    ],
    output: {
        filename: 'bundle.min.js',
        path: path.resolve(__dirname, 'static/dist')
    },
    resolve: {
        alias: {
            jquery: "jquery/src/jquery"
        }
    },
    module: {
        rules: [
            {
                test: /\.less$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: [
                        // {
                        //     loader: "style-loader" // creates style nodes from JS strings
                        // }, 
                        {
                            loader: "css-loader", // translates CSS into CommonJS
                            options: {
                                minimize: true
                            }
                        },
                        {
                            loader: "autoprefixer-loader?browsers=last 2 version"
                        }, 
                        {
                            loader: "less-loader" // compiles Less to CSS
                        }
                    ]
                })
                
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: [
                        {
                            loader: "css-loader",
                            options: {
                                minimize: true
                            }
                        }
                    ]
                })
            },
            {
                test: /fonts\/(.*)\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,   
                loader: "url-loader?limit=10000&mimetype=application/font-woff&name=[name].[ext]&outputPath=fonts/&publicPath=/static/dist/" 
            },
            { 
                test: /fonts\/(.*)\.ttf(\?v=[0-9]\.[0-9]\.[0-9])?$/,    
                loader: "url-loader?limit=10000&mimetype=application/octet-stream&name=[name].[ext]&outputPath=fonts/&publicPath=/static/dist/" 
            },
            { 
                test: /fonts\/(.*)\.eot(\?v=[0-9]\.[0-9]\.[0-9])?$/,    
                loader: "file-loader?name=[name].[ext]&outputPath=fonts/&publicPath=/static/dist/" 
            },
            { 
                test: /fonts\/(.*)\.svg(\?v=[0-9]\.[0-9]\.[0-9])?$/,    
                loader: "url-loader?limit=10000&mimetype=image/svg+xml&name=[name].[ext]&outputPath=fonts/&publicPath=/static/dist/" 
            },
            { 
                test: /bootstrap\/js\//, 
                loader: 'imports-loader?jQuery=jquery' 
            },
            {
                test: /\.coffee$/,
                use: ['coffee-loader']
            },
            {
                test: /\.(png|jpg|jpeg|svg|ico)$/i,
                use: [
                    {
                        loader: 'file-loader?name=[name].[ext]&outputPath=img/'
                    },
                    {
                        loader: 'image-webpack-loader?bypassOnDebug'
                    }
                ]
            },
            {
                test: /\.html$/,
                use: [
                    'ngtemplate-loader?relativeTo=/opt/project/static/src/',
                    'html-loader'
                ]
            }
            
        ],
        loaders: [
            
        ]
    },
    plugins: [
        new ExtractTextPlugin("styles.min.css"),
        new webpack.optimize.UglifyJsPlugin({
            compress: false,
            mangle: false,
            beautify: false
        }),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('prod')
        })
    ]
}